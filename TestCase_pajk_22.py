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
#https://baoxian.0033.com/web/products/gh_0007/index.html?id=50

starttime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#print('starttime:'+  starttime )

js_heigh = "var a=document.body.scrollHeight ;return(a)"
js_heigh_2 = "var b=document.documentElement.clientHeight ;return(b)"
js_2 = 'window.scrollBy(0,document.documentElement.clientHeight)'

#通过url请求接口，并将返回的内容存入字典并返回字典内容
kind = {0:'1',1:'2',2:'3',3:'4'}
url_head = 'https://baoxian.0033.com/insurance/v1/products?type=product&page=1&limit=20&kind=1%7C2%7C3%7C4%7C6&price_order=&tag_types=%22%22'

class ClassMethon(object):
    '''
        存放一些公共方法，方便后续进行调用
    '''
    imglist = []
    # 进入浏览器设置

    def setUp(self):
        options = webdriver.ChromeOptions()
        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(
            'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1/userid/366693514 isChrome/1')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(375, 812)  # 设置浏览器窗口大小
        self.driver.get('https://baoxian.0033.com/web/product-center.html')
        self.driver.implicitly_wait(20)#隐形等待二十
        if self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]'):
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]').click()
            #self.same_as('健康_')
            if self.driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]/ul/li[10]'):
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]/ul/li[10]').click()
                #self.same_as('平安e生保·住院医疗_')
                time.sleep(2)

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

    def same_as(self, na):
        # 截图
        fw = open('screenshot_path', 'w', encoding='utf8')  # 打开文件写入
        fr = open('screenshot_path', 'r', encoding='utf8')  # 打开文件读取
        t1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 获取当前的时间
        print('当前时间：' + t1)
        open('result', 'a', encoding='utf8').writelines('当前时间：' + t1 + '\n')
        # #day = t1[0:8]
        day = t1
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\baoxian\\pajk_22_平安e生保_住院医疗'
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

    def tearDown(self):
        self.driver.quit()




class baoxianxiangqing_pa_22(unittest.TestCase):
    classmethod = ClassMethon()
    classmethod.setUp()
    # 进入保险详情页面的操作
    def baoxianxiangqing_pa_22(self):

        if self.classmethod.find_by_class('typeChoose', None):
            # 这里的代码需要优化一下，查下自定义查找标签的方法,这里存在3个种类，可以用个循环

            for i in range(1,4):
                self.classmethod.find_by_xpath('/html/body/div[2]/div[2]/li['+ str(i)+']')
                self.classmethod.same_as('第'+str(i)+'选择_')
                time.sleep(1)
        #这里进行一下页面上课点击的操作的处理，先查看保障详情
        if self.classmethod.find_by_class('product_detail','click'):
            for i in range(1,4):#也是有三种选择
                self.classmethod.find_by_xpath('/html/body/div/div[1]/li[1'+ str(i)+']/span')
                self.classmethod.same_as('第'+str(i)+'选择_')
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
        self.classmethod.driver.quit()



class shisuanbaofei_pa_22(unittest.TestCase):
    classmethod = ClassMethon()
    classmethod.setUp()
    # 保费试算的操作内容
    def shisuanbaofei_pa_22(self):
        two_y = ['911 元', '349 元', '277 元', '174 元', '249 元', '307 元', '392 元', '484 元', '563 元', '915 元', '1123 元', '1438 元']
        six_y = ['999 元', '407 元', '321 元', '202 元', '271 元', '335 元', '427 元', '529 元', '617 元', '1004 元', '1232 元', '1579 元']
        two_n = ['1929 元', '641 元', '491 元', '329 元', '474 元', '659 元', '921 元', '1215 元', '1397 元', '2251 元', '3648 元', '3697 元']
        baofei = ['two_y', 'six_y', 'two_n']
        a = 0
        if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
            # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
            time.sleep(0.5)
            # 选择不同的类型进行点击操作
            for s in range(1,4):
                self.classmethod.find_by_xpath('/html/body/div[2]/div[8]/div/p[2]/em[' + str(s) + ']')
                for n in range(2, 14):  # 总共是13个价格选项
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[8]/div/p[5]/select')  # 点击展开年龄的选项
                    time.sleep(1.5)
                    self.classmethod.find_by_xpath('/html/body/div[2]/div[8]/div/p[5]/select/option[' + str(n) + ']')  # 选择指定的价格
                    time.sleep(1.5)
                    if self.classmethod.find_by_class('price', None):
                        price = self.classmethod.driver.find_element_by_class_name('price').text
                        if self.classmethod.driver.find_element_by_class_name('price').text == baofei[a][n - 2]:
                            print(str(s) + '_'+str(price) + '价格相同' + '\n')
                        else:
                            self.classmethod.same_as(str(s) + '_'+str(price)+'产品价格有误')
                a = a + 1

            self.classmethod.driver.quit()


class xiadan_pa_22(unittest.TestCase):
    classmethod = ClassMethon()
    classmethod.setUp()
    #下单流程的操作内容
    def xiadan_pa_22(self):
        name = '同花顺测试'
        telephone = '18868888588'
        idcard = '330724199401226219'
        bankno = '6228480323239098219'

        if self.classmethod.find_by_id('toubao'):  # 点击保费试算按钮
            # self.classmethod.driver.find_element_by_id('toubao').click()  # 点击弹窗展示
            time.sleep(1)
        self.classmethod.driver.find_element_by_id('toubao').click()  # 点击跳转下单流程页面
        self.classmethod.same_as('进入保单流程_')
        if self.classmethod.find_by_xpath('/html/body/div[1]/div/span[2]'):
            # 点击健康告知页面的【以上全否，继续投保】，进入保单填写页面
            #self.classmethod.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]').click()
            print('点击健康告知页面的按钮')
            time.sleep(1)
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
            #选择银行进行输入
            #不同的银行进行遍历一次
            self.classmethod.find_by_xpath('/html/body/div[2]/div[4]/li[2]/select')  # 点击展开银行的选项
            time.sleep(1.5)
            self.classmethod.find_by_xpath('/html/body/div[2]/div[4]/li[2]/select/option[3]')  # 选择指定的银行（这里银行有很多种，2-16,银行名称和卡号要一一对应起来）
            #输入银行卡号
            self.classmethod.driver.find_element_by_class_name('bankno').clear()
            self.classmethod.driver.find_element_by_class_name('bankno').send_keys(bankno)
            print('输入银行卡号')
            time.sleep(1)
            # 投保人选择自己
            # self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/li[2]/div/nav[1]').click()
            # print('投保人为本人')
            # 勾选协议
            time.sleep(1)
            self.classmethod.same_as('投保本人保单_')
            # driver.swipe(200,700,200,300)
            js = 'window.scrollTo(0,document.body.scrollHeight)'
            self.classmethod.driver.execute_script(js)  # 滑动页面到底部
            print('滑动页面到底部')
            time.sleep(1)
            self.classmethod.find_by_xpath('/html/body/div[2]/div[6]/p')
            #self.classmethod.driver.find_element_by_class_name('iconfont').click()  #
            print('点击勾选按钮')
            time.sleep(1)
            # 点击立即投保按钮，进去保险公司页面
            self.classmethod.driver.find_element_by_class_name('toubao').click()
            self.classmethod.same_as('保险公司_')
            time.sleep(2)
            self.classmethod.driver.quit()






if __name__ == '__main__':
    unittest.main()





