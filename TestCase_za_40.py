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


starttime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print('starttime:'+  starttime )

js_heigh = "var a=document.body.scrollHeight ;return(a)"
js_heigh_2 = "var b=document.documentElement.clientHeight ;return(b)"
js_2 = 'window.scrollBy(0,document.documentElement.clientHeight)'

#通过url请求接口，并将返回的内容存入字典并返回字典内容
kind = {0:'1',1:'2',2:'3',3:'4'}
url_head = 'https://baoxian.0033.com/insurance/v1/products?type=product&page=1&limit=20&kind=1%7C2%7C3%7C4%7C6&price_order=&tag_types=%22%22'


# # 进入浏览器设置
# options = webdriver.ChromeOptions()
# # 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# options.add_argument(
#     'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1/userid/366693514')
# driver = webdriver.Chrome(chrome_options=options)
# driver.set_window_size(375, 812)  # 设置浏览器窗口大小
# driver.get('https://baoxian.0033.com/web/products/za_0001/input.html?id=40')
# driver.implicitly_wait(15)


class ClassMethon(object):
    '''
        存放一些公共方法，方便后续进行调用
    '''

    imglist = []
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument(
        'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1/userid/366693514')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(375, 812)  # 设置浏览器窗口大小
    driver.get('https://baoxian.0033.com/web/product-center.html')
    driver.implicitly_wait(15)


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
        #fr = open('screenshot_path', 'r', encoding='utf8')  # 打开文件读取
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
        self.imglist.append(screen_save_path)
        fw.flush()
        fw.seek(0)
        return self.imglist

    def same_as(self, na):
        # 截图
        fw = open('screenshot_path', 'w', encoding='utf8')  # 打开文件写入
        fr = open('screenshot_path', 'r', encoding='utf8')  # 打开文件读取
        t1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 获取当前的时间
        print('当前时间：' + t1)
        open('result', 'a', encoding='utf8').writelines('当前时间：' + t1 + '\n')
        # #day = t1[0:8]
        day = t1
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\baoxian\\za_40手机资金安全险'
        # # 设定文件保存的路径，存放到当前目录下是screenshots文件夹中
        # print('当前的路径：' + img_folder)
        #open('result', 'a', encoding='utf8').writelines('当前的路径：' + img_folder + '\n')
        cre_file = ClassMethon()
        cre_file.creat_file(img_folder)
        screen_save_path = img_folder + '/' + na + t1 + '.png'  # 截屏图片命名方式
        #print('当前截图路径已经名称为：' + screen_save_path)
        open('result', 'a', encoding='utf8').writelines('当前截图路径已经名称为：' + screen_save_path + '\n')
        time.sleep(10)  # 休眠十秒等待页面加载完成
        self.driver.get_screenshot_as_file(screen_save_path)  # 截屏并存在指定的路径下
        #print('截图已存')
        open('result', 'a', encoding='utf8').writelines('截图已存 \n')
        #self.pic_save()
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
            #open('error', 'a', encoding='utf-8').writelines(e)


    def find_by_xpath(self,xpath):
        t = 0
        try:
           while t < 5:
               if self.driver.find_elements_by_xpath(xpath):
                   time.sleep(1)
                   self.driver.find_element_by_xpath(xpath).click()
                   return 1
               else:
                   time.sleep(1)
                   t = t + 1
           else:
               print('5s内未找到xpath')
               open('result', 'a', encoding='utf-8').writelines('5s内未找到xpath \n')
               return 0
        except Exception as e:
            print(e)
            #open('error', 'a', encoding='utf-8').writelines(e)


    def find_by_class(self, class_name, type):
        t = 0
        try:
            while t < 5:
                if self.driver.find_elements_by_class_name(class_name)and type =='click':
                    time.sleep(1)
                    self.driver.find_element_by_class_name(class_name).click()
                    return 1
                elif self.driver.find_elements_by_class_name(class_name)and type == None:

                    return 1

                else:
                    time.sleep(1)
                    t = t + 1
            else:
                print('5s内未找到id')
                open('result', 'a', encoding='utf8').writelines('5s内未找到class \n')
                return 0
        except Exception as e:
            print(e)
            #open('error', 'a', encoding='utf-8').writelines(e)


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
            open('error', 'a', encoding='utf-8').writelines(e)

    def get_bx_dic(self,url):
        request = urllib.request.Request(url)  # 请求目标url
        response = urllib.request.urlopen(request)  # 获取返回的结果
        data = response.read().decode('utf-8')  # 读取返回的结果并以utf-8进行编码
        data_dic = json.loads(data)  # 将返回的结果变成json读取，作为字典保存
        return data_dic

    # def f_rw(self,file_path,c):
    #     if c == 'w':
    #         fw = open(file_path, 'w', encoding='utf8')  # 打开文件写入
    #     if c == 'r':
    #         fr = open(file_path, 'r', encoding='utf8')  # 打开文件读取
    #     fw.writelines('c')
    #     open('result', 'w', encoding='utf8').writelines('')
    #     open('error', 'w', encoding='utf8').writelines('')





class SearchTestCase(unittest.TestCase):

    classmethod = ClassMethon()
    # def test_searchChina(self):
    #     """百度搜索中国的测试用例"""
    #     self.driver.find_element_by_xpath(".//*[@id='kw']").send_keys("中国")
    #     self.driver.find_element_by_xpath(".//*[@id='su']").click()
    #     WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(".//*[@id='1']/h3/a"))
    #     result = self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").text
    #     self.assertEqual(result, "中国_百度百科")

    # 开始执行用例
    # driver.set_window_size(fbl['iphone X'][0],fbl['iphone X'][1])  # 设置浏览器窗口大小

    # def shouyedemo(self):
    #     # 先判断页面是否打开了，查找某个控件来确认
    #
    #     # print(driver.execute_script(js_heigh))
    #     # print(driver.execute_script(js_heigh_2))
    #     t = math.ceil(self.driver.execute_script(js_heigh) // self.driver.execute_script(js_heigh_2)) + 1  # 向上取整
    #     # print(t)
    #     for i in range(1, t):
    #         # 截图并进行图像对比
    #         self.ClassMethon.same_as(i)
    #         self.driver.execute_script(js_2)
    #
    #     endtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    #     print('endtime:' + endtime)
    #     open('result', 'a', encoding='utf8').writelines('endtime:' + endtime + '\n')
    #     runtime = int(endtime) - int(starttime)
    #     print('runtime(s):' + str(runtime))
    #     open('result', 'a', encoding='utf8').writelines('runtime(s):' + str(runtime))
    #
    # def chanpingdemo(self):
    #
    #
    #     if self.find_by_class('footer-list-item', None):  # 判断是否能找到底部4个
    #         self.driver.find_elements_by_class_name('footer-list-item')[1].click()
    #         print('找到tab点击产品tab \n')
    #         open('result', 'a', encoding='utf8').writelines('找到tab点击产品tab \n')
    #         time.sleep(2)  # 等待2S，让页面加载出来
    #         self.same_as('产品_')
    #         if self.find_by_class('category-list', None):  # 查找首页，看是否存在产品
    #             for i in range(0, len(self.get_bx_dic(url_head)['data']['lists'])):  # 通过接口返回数据，确定存在多少类产品
    #                 time.sleep(2)
    #                 self.driver.find_elements_by_class_name('category-list-item')[i].click()
    #                 time.sleep(1)
    #                 self.same_as('产品_' + str(i))
    #                 time.sleep(1)
    #                 if self.find_by_class('hot-list', None):  # 判断是否存在产品
    #
    #                     x = len(self.get_bx_dic(url_head)['data']['lists'][kind[i]])  # 获取数量
    #                     for t in range(0,
    #                                    len(self.get_bx_dic(url_head)['data']['lists'][kind[i]])):  # 通过接口返回的内容判断数量长度
    #                         time.sleep(2)
    #                         # print(t)
    #                         cp_xpath = '/html/body/div[3]/div/ul/li[' + str(i + 1) + ']/ul/li[' + str(
    #                             t + 1) + ']'  # 拼接处xpath
    #                         self.driver.find_element_by_xpath(cp_xpath).click()  # 打开产品详情页面
    #
    #                         print('进入一个产品详情页面')
    #                         open('result', 'a', encoding='utf8').writelines('进入一个产品详情页面 \n')
    #                         time.sleep(1.5)
    #                         self.same_as('产品_' + str(i) + '_' + str(t) + '_')
    #                         self.driver.back()  # 回到上一页，产品列表页面
    #                         print('返回产品列表页面')
    #                         open('result', 'a', encoding='utf8').writelines('返回产品列表页面 \n')
    #                         time.sleep(2)
    #                         self.same_as('产品_')
    #                     time.sleep(2)
    #                     self.same_as('产品_')
    #                 time.sleep(2)
    #                 self.same_as('产品_')
    #     print('产品页面测试完成')
    #     open('result', 'a', encoding='utf8').writelines('产品页面测试完成 \n ')

    def case_za_40(self):
        name = '路人甲'
        telephone = '19957106219'
        idcard = '330724199401226219'

        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
                if self.classmethod.find_by_class('typeChoose', None):
                    # 这里的代码需要优化一下，查下自定义查找标签的方法
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[2]')
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('224元保五十万')
                    time.sleep(1)

                    # 滑动页面（计算页面高度和设备高度，一次滑动一屏幕，直至滑到底部）

                t = math.ceil(
                    self.classmethod.driver.execute_script(js_heigh) // self.classmethod.driver.execute_script(js_heigh_2)) + 1  # 向上取整
                for i in range(1, t):
                    # 截图并进行图像对比
                    self.classmethod.same_as('滑动第'+str(i) + '次_')
                    self.classmethod.driver.execute_script(js_2)
                # 滑到底部之后点击其他的按钮并进行截图

                if self.classmethod.find_by_class('zixun','click'):
                    #self.classmethod.driver.find_element_by_class_name('zixun').click()  # 点击咨询按钮
                    time.sleep(1)
                    self.classmethod.same_as('咨询页面')
                    self.classmethod.driver.back()  # 回到保险产品页面
                    time.sleep(1)
                    # 点击判断是否存在投保按钮，有的话点击
                    print('11111111111111111111111111111111调试资讯')
                if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                    #self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                    time.sleep(0.5)
                    print('1111111111111111')
                    # 选择不同的价格进行点击操作
                    if self.classmethod.find_by_class('product_info_2',None):  # 这边换个顺序进行点击操作，保证都是可以点击的
                        self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[2]').click()
                        self.classmethod.same_as('27元保五万')
                        self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[1]').click()
                        self.classmethod.same_as('6元保一万')
                        self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[3]').click()
                        self.classmethod.same_as('24元保五十万')
                        print('调试试算保费')
                    self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
                    self.classmethod.same_as('保单流程—')
                    if self.classmethod.find_by_xpath('/html/body/div[1]/div/span[2]'):
                        # 点击健康告知页面的【以上全否，继续投保】，进入保单填写页面
                        self.classmethod.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]').click()
                        print('点击健康告知页面的按钮')
                        time.sleep(2)
                    # screenshot(screenshot_dir, '继续投保按钮')
                    # 填写保单信息
                    if self.classmethod.find_by_title('保单填写'):
                        # 输入姓名，手机号，身份证号码
                        self.classmethod.driver.find_element_by_id('name').clear()
                        self.classmethod.driver.find_element_by_id('name').send_keys(name)
                        time.sleep(1)
                        print('输入名字')
                        self.classmethod.driver.find_element_by_id('telephone').clear()
                        self.classmethod.driver.find_element_by_id('telephone').send_keys(telephone)
                        time.sleep(1)
                        print('输入手机号')
                        self.classmethod.driver.find_element_by_id('idcard').clear()
                        self.classmethod.driver.find_element_by_id('idcard').send_keys(idcard)
                        print('输入身份证号码')
                        time.sleep(1)
                        # 投保人选择自己
                        # self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/li[2]/div/nav[1]').click()
                        # print('投保人为本人')
                        # 勾选协议
                        time.sleep(1)
                        self.classmethod.same_as('投保本人保单_')
                        # driver.swipe(200,700,200,300)
                        js = "window.scrollTo(0,document.body.scrollHeight)"
                        self.classmethod.driver.execute_script(js)  # 滑动页面到底部
                        print('滑动页面到底部')
                        time.sleep(1)
                        self.classmethod.driver.find_element_by_class_name('iconfont').click()  #
                        print('点击勾选按钮')
                        time.sleep(1)
                        # 点击立即投保按钮，进去保险公司页面
                        self.classmethod.driver.find_element_by_class_name('toubao').click()
                        self.classmethod.same_as('保险公司_')
                        self.classmethod.driver.close()


class baoxianxiangqing_za_40(unittest.TestCase):
    classmethod = ClassMethon()
    classmethod.driver.get('https://baoxian.0033.com/web/product-center.html')
    # 进入保险详情页面的操作
    def baoxianxiangqing_za_40(self):
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
                if self.classmethod.find_by_class('typeChoose', None):
                    # 这里的代码需要优化一下，查下自定义查找标签的方法
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[2]')
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('224元保五十万')
                    time.sleep(1)

                    # 滑动页面（计算页面高度和设备高度，一次滑动一屏幕，直至滑到底部）

                t = math.ceil(
                    self.classmethod.driver.execute_script(js_heigh) // self.classmethod.driver.execute_script(
                        js_heigh_2)) + 1  # 向上取整
                for i in range(1, t):
                    # 截图并进行图像对比
                    self.classmethod.same_as('滑动第' + str(i) + '次_')
                    self.classmethod.driver.execute_script(js_2)
                # 滑到底部之后点击其他的按钮并进行截图

                if self.classmethod.find_by_class('zixun', 'click'):
                    # self.classmethod.driver.find_element_by_class_name('zixun').click()  # 点击咨询按钮
                    time.sleep(1)
                    self.classmethod.same_as('咨询页面')
                    self.classmethod.driver.back()  # 回到保险产品页面
                    time.sleep(1)
                    # 点击判断是否存在投保按钮，有的话点击
                    self.classmethod.driver.back()

class shisuanbaofei_za_40(unittest.TestCase):
    classmethod = ClassMethon()
    classmethod.driver.get('https://baoxian.0033.com/web/product-center.html')
    # 保费试算的操作内容
    def shisuanbaofei_za_40(self):
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
            if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                time.sleep(0.5)
                print('1111111111111111')
                # 选择不同的价格进行点击操作
                if self.classmethod.find_by_class('product_info_2', None):  # 这边换个顺序进行点击操作，保证都是可以点击的
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[2]').click()
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[1]').click()
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[3]').click()
                    self.classmethod.same_as('24元保五十万')
                    print('调试试算保费')
                self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
                self.classmethod.same_as('进入保单流程_')
                self.classmethod.driver.back()


class xiadan_za_40(unittest.TestCase):
    classmethod = ClassMethon()
    #下单流程的操作内容
    def xiadan_za_40(self):
        name = '同花顺测试'
        telephone = '18868888588'
        idcard = '330724199401226219'
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
            if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                time.sleep(0.5)
            self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
            self.classmethod.same_as('进入保单流程_')
            if self.classmethod.find_by_xpath('/html/body/div[1]/div/span[2]'):
                # 点击健康告知页面的【以上全否，继续投保】，进入保单填写页面
                self.classmethod.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]').click()
                print('点击健康告知页面的按钮')
                time.sleep(2)
            # screenshot(screenshot_dir, '继续投保按钮')
            # 填写保单信息
            if self.classmethod.find_by_title('保单填写'):
                # 输入姓名，手机号，身份证号码
                self.classmethod.driver.find_element_by_id('name').clear()
                self.classmethod.driver.find_element_by_id('name').send_keys(name)
                time.sleep(1)
                print('输入名字')
                self.classmethod.driver.find_element_by_id('telephone').clear()
                self.classmethod.driver.find_element_by_id('telephone').send_keys(telephone)
                time.sleep(1)
                print('输入手机号')
                self.classmethod.driver.find_element_by_id('idcard').clear()
                self.classmethod.driver.find_element_by_id('idcard').send_keys(idcard)
                print('输入身份证号码')
                time.sleep(1)
                # 投保人选择自己
                # self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/li[2]/div/nav[1]').click()
                # print('投保人为本人')
                # 勾选协议
                time.sleep(1)
                self.classmethod.same_as('投保本人保单_')
                # driver.swipe(200,700,200,300)
                js = "window.scrollTo(0,document.body.scrollHeight)"
                self.classmethod.driver.execute_script(js)  # 滑动页面到底部
                print('滑动页面到底部')
                time.sleep(1)
                self.classmethod.driver.find_element_by_class_name('iconfont').click()  #
                print('点击勾选按钮')
                time.sleep(1)
                # 点击立即投保按钮，进去保险公司页面
                self.classmethod.driver.find_element_by_class_name('toubao').click()
                self.classmethod.same_as('保险公司_')
                self.classmethod.driver.close()



#第一次用例分割独立执行（需要进行封装处理，每次的步骤都有点长啊·重复的代码其实有很多·需要简化一下代码# ）
class SearchTestCase1(unittest.TestCase):
    classmethod = ClassMethon()


    #进入保险详情页面的操作
    def baoxianxiangqing_za_40(self):
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
                if self.classmethod.find_by_class('typeChoose', None):
                    # 这里的代码需要优化一下，查下自定义查找标签的方法
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[2]')
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('224元保五十万')
                    time.sleep(1)

                    # 滑动页面（计算页面高度和设备高度，一次滑动一屏幕，直至滑到底部）

                t = math.ceil(
                    self.classmethod.driver.execute_script(js_heigh) // self.classmethod.driver.execute_script(js_heigh_2)) + 1  # 向上取整
                for i in range(1, t):
                    # 截图并进行图像对比
                    self.classmethod.same_as('滑动第'+str(i) + '次_')
                    self.classmethod.driver.execute_script(js_2)
                # 滑到底部之后点击其他的按钮并进行截图

                if self.classmethod.find_by_class('zixun','click'):
                    #self.classmethod.driver.find_element_by_class_name('zixun').click()  # 点击咨询按钮
                    time.sleep(1)
                    self.classmethod.same_as('咨询页面')
                    self.classmethod.driver.back()  # 回到保险产品页面
                    time.sleep(1)
                    # 点击判断是否存在投保按钮，有的话点击


    classmethod = ClassMethon()
    #保费试算的操作内容
    def shisuanbaofei_za_40(self):
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
            if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                time.sleep(0.5)
                print('1111111111111111')
                # 选择不同的价格进行点击操作
                if self.classmethod.find_by_class('product_info_2', None):  # 这边换个顺序进行点击操作，保证都是可以点击的
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[2]').click()
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[1]').click()
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[3]').click()
                    self.classmethod.same_as('24元保五十万')
                    print('调试试算保费')
                self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
                self.classmethod.same_as('进入保单流程_')



    classmethod = ClassMethon()
    #下单流程的操作内容
    def xiadan_za_40(self):
        name = '同花顺测试'
        telephone = '18868888588'
        idcard = '330724199401226219'
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
            if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                time.sleep(0.5)
            self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
            self.classmethod.same_as('进入保单流程_')
            if self.classmethod.find_by_xpath('/html/body/div[1]/div/span[2]'):
                # 点击健康告知页面的【以上全否，继续投保】，进入保单填写页面
                self.classmethod.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]').click()
                print('点击健康告知页面的按钮')
                time.sleep(2)
            # screenshot(screenshot_dir, '继续投保按钮')
            # 填写保单信息
            if self.classmethod.find_by_title('保单填写'):
                # 输入姓名，手机号，身份证号码
                self.classmethod.driver.find_element_by_id('name').clear()
                self.classmethod.driver.find_element_by_id('name').send_keys(name)
                time.sleep(1)
                print('输入名字')
                self.classmethod.driver.find_element_by_id('telephone').clear()
                self.classmethod.driver.find_element_by_id('telephone').send_keys(telephone)
                time.sleep(1)
                print('输入手机号')
                self.classmethod.driver.find_element_by_id('idcard').clear()
                self.classmethod.driver.find_element_by_id('idcard').send_keys(idcard)
                print('输入身份证号码')
                time.sleep(1)
                # 投保人选择自己
                # self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/li[2]/div/nav[1]').click()
                # print('投保人为本人')
                # 勾选协议
                time.sleep(1)
                self.classmethod.same_as('投保本人保单_')
                # driver.swipe(200,700,200,300)
                js = "window.scrollTo(0,document.body.scrollHeight)"
                self.classmethod.driver.execute_script(js)  # 滑动页面到底部
                print('滑动页面到底部')
                time.sleep(1)
                self.classmethod.driver.find_element_by_class_name('iconfont').click()  #
                print('点击勾选按钮')
                time.sleep(1)
                # 点击立即投保按钮，进去保险公司页面
                self.classmethod.driver.find_element_by_class_name('toubao').click()
                self.classmethod.same_as('保险公司_')
                self.classmethod.driver.close()


#第一次用例分割独立执行（需要进行封装处理，每次的步骤都有点长啊·重复的代码其实有很多·需要简化一下代码# ）
class SearchTestCase2(unittest.TestCase):
    classmethod = ClassMethon()

    def setUp(self):
        options = webdriver.ChromeOptions()
        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(
            'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1/userid/366693514')
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_window_size(375, 812)  # 设置浏览器窗口大小
        driver.get('https://baoxian.0033.com/web/product-center.html')
        driver.implicitly_wait(15)

    #进入保险详情页面的操作
    def baoxianxiangqing_za_40(self):
        self.setUp()
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
                if self.classmethod.find_by_class('typeChoose', None):
                    # 这里的代码需要优化一下，查下自定义查找标签的方法
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[2]')
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li[1]')
                    self.classmethod.same_as('224元保五十万')
                    time.sleep(1)

                    # 滑动页面（计算页面高度和设备高度，一次滑动一屏幕，直至滑到底部）

                t = math.ceil(
                    self.classmethod.driver.execute_script(js_heigh) // self.classmethod.driver.execute_script(js_heigh_2)) + 1  # 向上取整
                for i in range(1, t):
                    # 截图并进行图像对比
                    self.classmethod.same_as('滑动第'+str(i) + '次_')
                    self.classmethod.driver.execute_script(js_2)
                # 滑到底部之后点击其他的按钮并进行截图

                if self.classmethod.find_by_class('zixun','click'):
                    #self.classmethod.driver.find_element_by_class_name('zixun').click()  # 点击咨询按钮
                    time.sleep(1)
                    self.classmethod.same_as('咨询页面')
                    self.classmethod.driver.back()  # 回到保险产品页面
                    time.sleep(1)
                    # 点击判断是否存在投保按钮，有的话点击


    #保费试算的操作内容
    def shisuanbaofei_za_40(self):
        self.setUp()
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
            if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                time.sleep(0.5)
                print('1111111111111111')
                # 选择不同的价格进行点击操作
                if self.classmethod.find_by_class('product_info_2', None):  # 这边换个顺序进行点击操作，保证都是可以点击的
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[2]').click()
                    self.classmethod.same_as('27元保五万')
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[1]').click()
                    self.classmethod.same_as('6元保一万')
                    self.classmethod.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[3]').click()
                    self.classmethod.same_as('24元保五十万')
                    print('调试试算保费')
                self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
                self.classmethod.same_as('进入保单流程_')


    #下单流程的操作内容
    def xiadan_za_40(self):
        self.setUp()
        name = '同花顺测试'
        telephone = '18868888588'
        idcard = '330724199401226219'
        if self.classmethod.find_by_xpath('/html/body/div[2]/div[1]/ul/li[4]'):
            time.sleep(1)
            self.classmethod.same_as('财产_')
            if self.classmethod.find_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li'):
                time.sleep(1)
                self.classmethod.same_as('众安手机资金安全险_')
                time.sleep(2)
            if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
                # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
                time.sleep(0.5)
            self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
            self.classmethod.same_as('进入保单流程_')
            if self.classmethod.find_by_xpath('/html/body/div[1]/div/span[2]'):
                # 点击健康告知页面的【以上全否，继续投保】，进入保单填写页面
                self.classmethod.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]').click()
                print('点击健康告知页面的按钮')
                time.sleep(2)
            # screenshot(screenshot_dir, '继续投保按钮')
            # 填写保单信息
            if self.classmethod.find_by_title('保单填写'):
                # 输入姓名，手机号，身份证号码
                self.classmethod.driver.find_element_by_id('name').clear()
                self.classmethod.driver.find_element_by_id('name').send_keys(name)
                time.sleep(1)
                print('输入名字')
                self.classmethod.driver.find_element_by_id('telephone').clear()
                self.classmethod.driver.find_element_by_id('telephone').send_keys(telephone)
                time.sleep(1)
                print('输入手机号')
                self.classmethod.driver.find_element_by_id('idcard').clear()
                self.classmethod.driver.find_element_by_id('idcard').send_keys(idcard)
                print('输入身份证号码')
                time.sleep(1)
                # 投保人选择自己
                # self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/li[2]/div/nav[1]').click()
                # print('投保人为本人')
                # 勾选协议
                time.sleep(1)
                self.classmethod.same_as('投保本人保单_')
                # driver.swipe(200,700,200,300)
                js = "window.scrollTo(0,document.body.scrollHeight)"
                self.classmethod.driver.execute_script(js)  # 滑动页面到底部
                print('滑动页面到底部')
                time.sleep(1)
                self.classmethod.driver.find_element_by_class_name('iconfont').click()  #
                print('点击勾选按钮')
                time.sleep(1)
                # 点击立即投保按钮，进去保险公司页面
                self.classmethod.driver.find_element_by_class_name('toubao').click()
                self.classmethod.same_as('保险公司_')
                self.classmethod.driver.close()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



'''
def xiangqing_za_40(self):  # 众安保险--手机资金安全险
   '''
# 打开保险产品中心页面，进入产品详情页面并截图
# 点击三个不同的价格，并且截图
# 滑动页面，直至滑到底部，并且截图
# 点击咨询，并截图然后点击返回按钮回到上一页
# 点击机器人按钮，截图并返回上一页
#打开保险产品中心页面，进入保险详情页面-点击试算保费按钮
# 点击【试算保费】按钮并截图
# 循环点击不同的价格并截图，选择任意一个价格点击
# 点击立即投保按钮，进入投保流程页面
#打开保险产品中心页面，进入保险详情页面，点击保费试算，点击下单流程
# :param url:
# :return:
'''

#url = 'https://baoxian.0033.com/web/products/za_0001/index.html?id=40'
# 打开先截图
self.classmethod.same_as('众安手机资金安全险')
if self.classmethod.find_by_class('typeChoose', None):
    # 这里的代码需要优化一下，查下自定义查找标签的方法
    self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/li[1]').click()
    self.classmethod.same_as('6元保一万')
    self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/li[2]').click()
    self.classmethod.same_as('27元保五万')
    self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/li[1]').click()
    self.classmethod.same_as('224元保五十万')
    time.sleep(1)

    # 滑动页面（计算页面高度和设备高度，一次滑动一屏幕，直至滑到底部）

t = math.ceil(self.driver.execute_script(js_heigh) // self.driver.execute_script(js_heigh_2)) + 1  # 向上取整
for i in range(1, t):
    # 截图并进行图像对比
    self.classmethod.same_as(i)
    self.driver.execute_script(js_2)
# 滑到底部之后点击其他的按钮并进行截图

if self.classmethod.find_by_class('zixun'):
    self.driver.find_element_by_class_name('zixun').click()  # 点击咨询按钮
    time.sleep(1)
    self.classmethod.same_as('咨询页面')
    self.driver.back()  # 回到保险产品页面
    time.sleep(1)
    # 点击判断是否存在投保按钮，有的话点击

if self.classmethod.find_by_class('toubao'):  # 点击保费试算按钮
    self.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
    time.sleep(0.5)
    # 选择不同的价格进行点击操作
    if self.classmethod.find_by_class('product_info_2'):  # 这边换个顺序进行点击操作，保证都是可以点击的
        self.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[2]').click()
        self.classmethod.same_as('27元保五万')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[1]').click()
        self.classmethod.same_as('6元保一万')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[3]').click()
        self.classmethon.same_as('224元保五十万')

    self.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
    self.classmethon.same_as('保单流程—')

def order_za_40(self):  # 众安保险--手机资金安全险下单页面

# self.xiangqing_za_40()
name = '路人甲'
telephone = '19957106219'
idcard = '330724199401226219'
# 健康告知页面,这里的xpath还需要在确认下
if self.classmethod.find_by_xpath('/html/body/div[1]/div/span[2]'):
    # 点击健康告知页面的【以上全否，继续投保】，进入保单填写页面
    self.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]').click()
    print('点击健康告知页面的按钮')
    time.sleep(2)
# screenshot(screenshot_dir, '继续投保按钮')
# 填写保单信息
if self.classmethod.find_by_title('保单填写'):
    # 输入姓名，手机号，身份证号码
    self.driver.find_element_by_id('name').clear()
    self.driver.find_element_by_id('name').send_keys(name)
    time.sleep(1)
    print('输入名字')
    self.driver.find_element_by_id('telephone').clear()
    self.driver.find_element_by_id('telephone').send_keys(telephone)
    time.sleep(1)
    print('输入手机号')
    self.driver.find_element_by_id('idcard').clear()
    self.driver.find_element_by_id('idcard').send_keys(idcard)
    print('输入身份证号码')
    time.sleep(1)
    # 投保人选择自己
    # self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/li[2]/div/nav[1]').click()
    # print('投保人为本人')
    # 勾选协议
    time.sleep(1)
    self.classmethod.same_as('投保本人保单_')
    # driver.swipe(200,700,200,300)
    js = "window.scrollTo(0,document.body.scrollHeight)"
    self.driver.execute_script(js)  # 滑动页面到底部
    print('滑动页面到底部')
    time.sleep(1)
    self.driver.find_element_by_class_name('iconfont').click()  #
    print('点击勾选按钮')
    time.sleep(1)
    # 点击立即投保按钮，进去保险公司页面
    self.driver.find_element_by_class_name('toubao').click()
    self.same_as('保险公司_')
    self.driver.close()
    self.driver.quit()


 '''


