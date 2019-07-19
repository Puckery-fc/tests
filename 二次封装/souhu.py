# -*- coding: utf-8 -*-
# File  : souhu.py
# Date  : 2018/9/7

from selenium import webdriver
import unittest,time

class test_souhu(unittest.TestCase):
    u"登录"
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://www.sohu.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text("登录狐友").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]").click()
        time.sleep(3)
        
    def login(self,user,password):
        u"账号密码参数化"
        self.driver.find_element_by_class_name("user-input").send_keys(user)
        #time.sleep(3)
        self.driver.find_element_by_class_name("password-input").send_keys(password)
        #time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[2]/input").click()
    
    def login_sucess(self):
        u"判断是否获取到登录账号"
        try:
            text = self.driver.find_element_by_class_name("name").text
            print(text)
            return True
        except:
            return False
            
    def test_01(self):
        u"登录案例1"
        self.login(u"15088558058","fc678268")
        result = self.login_sucess()
        self.assertTrue(result)
        title = self.driver.title
        print(title)
    
    def test_02(self):
        u"登录案例2"
        self.login(u"15088558058@souhu.com","fc678268")
        result = self.login_sucess()
        self.assertTrue(result)
        title = self.driver.title
        print(title)
        
    def tearDown(self):
        self.driver.quit()
            
            
if __name__ == '__main__':
    unittest.main()

        