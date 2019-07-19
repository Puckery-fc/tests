# -*- coding: utf-8 -*-
# File  : Login.py
# Date  : 2019/4/28
from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time,os,unittest

class JD(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.jd.com/"
        
    def test_Login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        cookieBefore = driver.get_cookies()
        print(cookieBefore) #打印登录前的cookie
        time.sleep(2)
        driver.find_element_by_class_name("link-login").click()
        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys("15088558058")
        driver.find_element_by_id("loginname").send_keys(Keys.TAB)
        driver.find_element_by_id("nloginpwd").send_keys("fc678268")
        driver.find_element_by_id("loginsubmit").click()
        driver.implicitly_wait(5) # 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
        time.sleep(5)
        print("登录后")
        cookieAfter = driver.get_cookies()
        print("cookiesAfter:")
        print(cookieAfter)
        len1 = len(cookieAfter)
        print("len:%d"%len1)
        cookie1 = cookieAfter[0]
        cookie2 = cookieAfter[3]
        cookie3 = cookieAfter[-2]
        cookie4 = cookieAfter[-1]
        print("cookie1:%s"%cookie1)
        print("cookie2:%s" % cookie2)
        print("cookie3:%s" % cookie3)
        print("cookie4:%s" % cookie4)
        driver.quit()
        # 将获取的这四个cookie作为参数，传递给，使用cookie登录的函数，如下
        cookieLogin(cookie1,cookie2,cookie3,cookie4)
    def cookieLogin(cookie1,cookie2,cookie3,cookie4):
        print("+++++++++++++++++++++++++")
        print("cookieLogin")
        print("cookie2:%s" % cookie2)
        print("cookie4:%s" % cookie4)
        driver = self.driver
        driver.maximize_window()
        driver.delete_all_cookies()
        time.sleep(3)
        driver.get(self.base_url)
        driver.add_cookie(cookie1)
        driver.add_cookie(cookie2)
        driver.add_cookie(cookie3)
        driver.add_cookie(cookie4)
        print("cookies")
        print(driver.get_cookies())
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()
    

