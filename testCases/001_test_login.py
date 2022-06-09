import unittest
from selenium import webdriver
import sys
sys.path.append('ecshop自动化测试\\public\\')
from common import *

#定义一个Mytest类，继承了unittest里面的TestCase类
class Mytest(unittest.TestCase):

    #初始化环境，类似用例的预置条件,提前准备测试数据
    def setUp(self):
        #调用common模块的打开网址的函数
        open_web(self)
        
    #登陆用例,用例的方法名必须以test开头,执行顺序1-9，a-z
    def test_login(self):
        #调用common模块的登陆
        login(self,'yyyyyy','yyyyyy')
        #定义变量hope_result,是期望结果
        hope_result = 'yyyyyy'
        #定义变量reality_result，是实际结果
        reality_result = self.dr.find_element_by_xpath('//*[@class="f4_b"]').text
        #相等断言
        self.assertEqual(hope_result,reality_result)

        
    #恢复环境，一般用于退出浏览器，清理测试数据
    def tearDown(self):
        self.dr.quit()
        
if __name__=='__main__':
    #执行所有的测试用例
    unittest.main()
