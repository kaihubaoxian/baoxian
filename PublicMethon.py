import os
import operator
import time
import math
import urllib
import json
import urllib.request
import unittest
from PIL import Image
from pandas.compat import reduce
from selenium import webdriver
#from baoxian.TestCase import SearchTestCase

imglist = []
class ClassMethon(unittest.TestCase):
    '''
        存放一些公共方法，方便后续进行调用
    '''


    def setUp(self):
        # 进入浏览器设置
        options = webdriver.ChromeOptions()
        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(
            'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1/userid/366693514')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(375, 812)  # 设置浏览器窗口大小
        self.driver.get('https://baoxian.0033.com/web/products/za_0001/input.html?id=40')
        self.driver.implicitly_wait(15)

    def creat_file(self,path):
        #t1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 获取当前的时间
        #print('当前时间：' + t1)
        #day = t1[0:8]
        #img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/screenshot'
        # 设定文件保存的路径，存放到当前目录下是screenshots文件夹中
        #print('当前的路径：' + img_folder)
        #path = img_folder + '/'

        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print(path + ' 创建成功')
            open('result', 'a', encoding='utf8').writelines(path + ' 创建成功' + '\n')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            open('result', 'a', encoding='utf8').writelines(path + ' 目录已存在' + '\n')
            return False

    def pic_save(self, na):
        # 截图
        fw = open('screenshot_path', 'w', encoding='utf8')  # 打开文件写入
        fr = open('screenshot_path', 'r', encoding='utf8')  # 打开文件读取
        t1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 获取当前的时间
        print('当前时间：' + t1)
        open('result', 'a', encoding='utf8').writelines('当前时间：' + t1 + '\n')
        day = t1[0:8]
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\screenshot'
        # 设定文件保存的路径，存放到当前目录下是screenshots文件夹中

        print('当前的路径：' + img_folder)
        open('result', 'a', encoding='utf8').writelines('当前的路径：' + img_folder + '\n')
        screen_save_path = img_folder + '/' + day + '/' + t1 + na + '.png'  # 截屏图片命名方式

        print('当前截图路径已经名称为：' + screen_save_path)
        open('result', 'a', encoding='utf8').writelines('当前截图路径已经名称为：' + screen_save_path + '\n')
        time.sleep(3)  # 休眠十秒等待页面加载完成
        self.driver.get_screenshot_as_file(screen_save_path)  # 截屏并存在指定的路径下

        print('截图已存')
        open('result', 'a', encoding='utf8').writelines('截图已存 \n')
        fw.writelines(screen_save_path + '\n')
        imglist.append(screen_save_path)
        fw.flush()
        fw.seek(0)
        return self.imglist

    def same_as(self,na):
        # 截图
        # fw = open('screenshot_path', 'w', encoding='utf8')  # 打开文件写入
        # fr = open('screenshot_path', 'r', encoding='utf8')  # 打开文件读取
        # t1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 获取当前的时间
        # print('当前时间：' + t1)
        # open('result', 'a', encoding='utf8').writelines('当前时间：' + t1 + '\n')
        # #day = t1[0:8]
        # day = t1
        # img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\screenshot'
        # # 设定文件保存的路径，存放到当前目录下是screenshots文件夹中
        # print('当前的路径：' + img_folder)
        # open('result', 'a', encoding='utf8').writelines('当前的路径：' + img_folder + '\n')
        # cre_file = ClassMethon()
        # cre_file.creat_file(img_folder)
        # screen_save_path = img_folder + '/' + na + t1 + '.png'  # 截屏图片命名方式
        # print('当前截图路径已经名称为：' + screen_save_path)
        # open('result', 'a', encoding='utf8').writelines('当前截图路径已经名称为：' + screen_save_path + '\n')
        # time.sleep(10)  # 休眠十秒等待页面加载完成
        # self.driver.get_screenshot_as_file(screen_save_path)  # 截屏并存在指定的路径下
        # print('截图已存')
        # open('result', 'a', encoding='utf8').writelines('截图已存 \n')
        self.pic_save(na)
        imglist = self.imglist
        if len(imglist) > 1:
            #这里的 screen_save_path 和 imglist[i] 是同一个张图片
            image1 = Image.open(imglist[-2])
            image2 = Image.open(imglist[-1])
            # 把图像对象转换为直方图数据，存在list h1、h2 中s
            h1 = image1.histogram()
            h2 = image2.histogram()
            result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))  #通过方差大小进行计算
            print(result)
            if result > 5:
                # 图像不一致，继续执行下一个下拉截图
                print(imglist[-1] + '与' + imglist[-2] + '张图像不一致,继续执行。')
                open('result', 'a', encoding='utf8').writelines(imglist[-1] + '与' + imglist[-2] + '张图像不一致,继续执行。' + '\n')
            else:
                # 图像一致，判断一致原因
                print(imglist[-1] + '与' + imglist[-2] + '图像一致')
                open('result', 'a', encoding='utf8').writelines(imglist[-1] + '与' + imglist[-2] + '图像一致' + '\n')
                if self.driver.title != '同花顺保险':
                    print('跳转地址有误,返回上一张图的位置重新截图')
                    open('result', 'a', encoding='utf8').writelines('跳转地址有误,返回上一张图的位置重新截图 \n')

    def find_by_id(self,id):
        t = 0
        try:
           while t < 5:
                if self.driver.find_elements_by_id(id):
                    self.driver.find_element_by_id(id).click()
                    return 1
                else:
                    time.sleep(1)
                    t = t + 1
           else:
               print('5s内未找到id')
               open('result', 'a', encoding='utf8').writelines('5s内未找到id \n')
               return 0
        except Exception as e:
            print(e)
            open('error', 'a', encoding='utf8').writelines(e + '\n')


    def find_by_xpath(self,xpath):
        t = 0
        try:
           while t < 5:
               if self.driver.find_elements_by_xpath(xpath):
                   self.driver.find_element_by_xpath(xpath).click()
                   return 1
               else:
                   time.sleep(1)
                   t = t + 1
           else:
               print('5s内未找到xpath')
               open('result', 'a', encoding='utf8').writelines('5s内未找到xpath \n')
               return 0
        except Exception as e:
            print(e)
            open('error', 'a', encoding='utf8').writelines(e + '\n')


    def find_by_class(self, class_name, type):
        t = 0
        try:
            while t < 5:
                if self.driver.find_elements_by_class_name(class_name)and type =='click':
                    self.driver.find_element_by_class_name(class_name).click()
                    return 1
                elif self.driver.find_elements_by_class_name(class_name)and type == None:

                    return 1

                else:
                    time.sleep(1)
                    t = t + 1
            else:
                print('5s内未找到id')
                open('result', 'a', encoding='utf8').writelines('5s内未找到id \n')
                return 0
        except Exception as e:
            print(e)
            open('error', 'a', encoding='utf8').writelines(e + '\n')


    def find_by_title(self,title):
        t = 0
        try:
            while t < 5:
                if self.driver.title == title:
                    return 1
                else:
                    time.sleep(1)
                    t = t + 1
            else:
                #print('5s内未找到id')
                open('result', 'a', encoding='utf8').writelines('未找到该标题 \n')
                return 0
        except Exception as e:
            print(e)
            open('error', 'a', encoding='utf8').writelines(e + '\n')

    def get_bx_dic(self,url):
        request = urllib.request.Request(url)  # 请求目标url
        response = urllib.request.urlopen(request)  # 获取返回的结果
        data = response.read().decode('utf-8')  # 读取返回的结果并以utf-8进行编码
        data_dic = json.loads(data)  # 将返回的结果变成json读取，作为字典保存
        return data_dic

    def f_rw(self,file_path,c):
        if c == 'w':
            fw = open(file_path, 'w', encoding='utf8')  # 打开文件写入
        if c == 'r':
            fr = open(file_path, 'r', encoding='utf8')  # 打开文件读取
        fw.writelines('c')
        open('result', 'w', encoding='utf8').writelines('')
        open('error', 'w', encoding='utf8').writelines('')