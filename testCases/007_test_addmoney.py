import unittest
from selenium import webdriver
import sys
sys.path.append('ecshop自动化测试\\public\\')
from common import *
from time import sleep
from selenium.webdriver.common.by import By
import os


if __name__ == '__main__': 
    program = os.path.basename(sys.argv[0])


#定义一个Mytest类，继承了unittest里面的TestCase类
class Mytest(unittest.TestCase):

    #初始化环境，类似用例的预置条件,提前准备测试数据
    def setUp(self):
        #调用common模块的打开网址的函数
        open_web(self)
        self.dr.implicitly_wait(5)
        
    #登陆用例,用例的方法名必须以test开头,执行顺序1-9，a-z
    def test_addmoney(self):

        print('\n'+program+' is running ------------------------------------------\n')
        Step=1

        print('\nStep',str(Step)+': login\n')
        Step=Step+1
        #调用common模块的登陆
        login(self,'yyyyyy','yyyyyy')

        print('\nStep',str(Step)+': click\n')
        Step=Step+1
        self.dr.find_element(By.XPATH,'/html/body/div[8]/div/div/dl[4]/dd[1]/a').click()

        print('\nStep',str(Step)+': add\n')
        Step=Step+1
        self.dr.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div/table[1]/tbody/tr/td/a[1]').click()

        print('\nStep',str(Step)+': submit\n')
        Step=Step+1
        self.dr.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div/form/table[1]/tbody/tr[1]/td[2]/input').send_keys('777')
        self.dr.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div/form/table[1]/tbody/tr[2]/td[2]/textarea').send_keys('777')
        self.dr.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div/form/table[2]/tbody/tr[4]/td[1]/input').click()
        self.dr.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div/form/table[2]/tbody/tr[5]/td/input[4]').click()

        print('\nStep',str(Step)+': judge\n')
        Step=Step+1
        #定义变量hope_result,是期望结果
        hope_result = '777'
        #定义变量reality_result，是实际结果
        reality_result = self.dr.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div/table/tbody/tr[1]/td[2]').text
        #断言
        self.assertIn(hope_result,reality_result)

        
    #恢复环境，一般用于退出浏览器，清理测试数据
    def tearDown(self):
        sleep(1)
        self.dr.quit()
        
if __name__=='__main__':
    #执行所有的测试用例
    unittest.main()
