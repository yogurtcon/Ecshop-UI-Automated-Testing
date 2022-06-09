from selenium import webdriver
import pymysql
from selenium.webdriver.common.by import By
import sys
import os


if __name__ == '__main__': 
    program = os.path.basename(sys.argv[0])
    print(program)


def print_file_name(self):
    program = os.path.basename(sys.argv[0])
    print(program)


#封装打开网址的操作
def open_web(self):
    self.dr = webdriver.Edge()
    self.dr.get('http://192.168.2.233/ecshop')


#封装登陆的操作
def login(self,uname,passwd):
    self.dr.find_element(By.XPATH,'//*[@id="ECS_MEMBERZONE"]/a[1]').click()
    self.dr.find_element(By.XPATH,'//*[@name="username"]').send_keys(uname)
    self.dr.find_element(By.XPATH,'//*[@name="password"]').send_keys(passwd)
    self.dr.find_element(By.XPATH,'//*[@name="submit"]').click()

def execute_sql(sql):
    db = pymysql.connect('192.168.2.233','chen','123456','test')
    #定义变量cr，获取游标
    cr = db.cursor()
    #执行sql语句
    cr.execute(sql)
    #提交事务
    db.commit()
    #关闭数据库连接
    db.close()
    #关闭游标
    cr.close()
