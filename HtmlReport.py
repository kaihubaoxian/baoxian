import HTMLTestRunner

import unittest
from time import strftime, localtime, time
#from baoxian.TestCase_za_40_test import SearchTestCase
#from baoxian.TestCase_za_40 import SearchTestCase
#from baoxian.TestCase_za_40 import baoxianxiangqing_za_40
#from baoxian.TestCase_za_40 import shisuanbaofei_za_40
#from baoxian.TestCase_za_40 import xiadan_za_40
#from baoxian.TestCase_za_40 import SearchTestCase2
#from baoxian.TestCase_ghrs_50 import baoxianxiangqing_gh_50
#from baoxian.TestCase_ghrs_50 import shisuanbaofei_gh_50
#from baoxian.TestCase_ghrs_50 import xiadan_gh_50
from baoxian.TestCase_pajk_22 import baoxianxiangqing_pa_22
from baoxian.TestCase_pajk_22 import shisuanbaofei_pa_22
from baoxian.TestCase_pajk_22 import xiadan_pa_22

suite = unittest.TestSuite()
# 获取TestSuite的实例对象
#suite.addTest(ClassDemo('chanpingdemo'))

'''
这里进行用例的执行与操作，每个保险产品分三步，执行三个函数

'''



#suite.addTest(SearchTestCase('case_za_40'))
#suite.addTest(baoxianxiangqing_za_40('baoxianxiangqing_za_40'))
#suite.addTest(baoxianxiangqing_gh_50('baoxianxiangqing_gh_50'))
suite.addTest(baoxianxiangqing_pa_22('baoxianxiangqing_pa_22'))
suite.addTest(shisuanbaofei_pa_22('shisuanbaofei_pa_22'))
suite.addTest(xiadan_pa_22('xiadan_pa_22'))
#suite.addTest(xiadan_gh_50('xiadan_gh_50'))

#suite.addTest(xiadan_za_40('xiadan_za_40'))
#suite.addTest(SearchTestCase1('baoxianxiangqing_za_40'))

#suite.addTest(SearchTestCase1('shisuanbaofei_za_40'))

#suite.addTest(SearchTestCase1('xiadan_za_40'))
#suite.addTest(SearchTestCase('order_za_40'))

#suite.addTest(SearchTestCase('baoxianxiangqing_za_40'))

#suite.addTest(SearchTestCase('shisuanbaofei_za_40'))

#suite.addTest(SearchTestCase('xiadan_za_40'))
# 把测试用例添加到测试容器中

now = strftime("%Y-%m-%d-%H_%M_%S", localtime(time()))
# 获取当前时间
filename = now + "_test.html"
# 文件名

fp = open(filename, "wb")
# 以二进制的方式打开文件并写入结果
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title="平安e生保·住院医疗",
    description="测试报告的详情")

runner.run(suite)

fp.close()