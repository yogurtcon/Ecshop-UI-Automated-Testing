import unittest
from selenium import webdriver
from time import sleep
import sys
sys.path.append('ecshop自动化测试\\public\\')
from common import *

#定义一个Mytest类，继承了unittest里面的TestCase类
class Mytest(unittest.TestCase):

    #初始化环境，类似用例的预置条件,提前准备测试数据
    def setUp(self):
        #调用common模块的打开网址的函数
        open_web(self)
        self.dr.implicitly_wait(5)

    def test_shopping(self):
        login(self,'yyyyyy','yyyyyy')

        self.dr.find_element_by_xpath('//*[@id="show_best_area"]/div[3]/a').click()
        self.dr.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a').click()
        self.dr.find_element_by_xpath('//*[@id="shippingTable"]/tbody/tr[2]/td[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="paymentTable"]/tbody/tr[3]/td[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="theForm"]/div[15]/div[2]/input[1]').click()

        #定义实际结果，定位到邮箱的输入框元素，获取属性value的值
        reality_result = self.dr.find_element_by_xpath('/html/body/div[7]/div/h6').text
        #定义期望结果，是修改后的用户名
        hope_result='您的订单已提交成功'
        #断言
        self.assertIn(hope_result,reality_result)

    #恢复环境，一般用于退出浏览器，清理测试数据
    def tearDown(self):
        sleep(2)
        self.dr.quit()
        
if __name__=='__main__':
    #执行所有的测试用例
    unittest.main()

        
        
