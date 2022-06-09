import unittest
from selenium import webdriver
import sys
sys.path.append('ecshop自动化测试\\public\\')
from common import *
from time import sleep
from selenium.webdriver.common.by import By

#定义一个Mytest类，继承了unittest里面的TestCase类
class Mytest(unittest.TestCase):

    #初始化环境，类似用例的预置条件,提前准备测试数据
    def setUp(self):
        #调用common模块的打开网址的函数
        open_web(self)
        self.dr.implicitly_wait(5)
        
    #登陆用例,用例的方法名必须以test开头,执行顺序1-9，a-z
    def test_allDelete(self):
        #调用common模块的登陆
        login(self,'yyyyyy','yyyyyy')

        self.dr.find_element(By.XPATH,'//*[@id="show_best_area"]/div[3]/a').click()
        self.dr.find_element(By.XPATH,'//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]').click()

        print('\n\n清空购物车\n\n')
        self.dr.find_element(By.XPATH,'//*[@id="formCart"]/table[2]/tbody/tr/td[2]/input[1]').click()

        #定义变量hope_result,是期望结果
        hope_result = '您的购物车中有 0 件商品'
        #定义变量reality_result，是实际结果
        reality_result = self.dr.find_element(By.XPATH,'//*[@id="ECS_CARTINFO"]/a').text
        #断言
        self.assertIn(hope_result,reality_result)

        
    #恢复环境，一般用于退出浏览器，清理测试数据
    def tearDown(self):
        sleep(1)
        self.dr.quit()
        
if __name__=='__main__':
    #执行所有的测试用例
    unittest.main()
