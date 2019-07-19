# -*- coding: utf-8 -*-
# File  : test_baidulogin.py
# Date  : 2019/5/29

# 验证码不会
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Page(object):
    login_url = "https://www.baidu.com"
    
    def __init__(self,base_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = base_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        # self.driver.implicitly_wait(10)
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)
        
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

class LoginPage(Page):
    url = "/"
    username_loc = (By.ID,"TANGRAM__PSP_10__userName")
    pwd_loc = (By.ID,"TANGRAM__PSP_10__password")
    login_loc = (By.ID,"TANGRAM__PSP_10__submit")
    
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    
    def type_pwd(self,pwd):
        self.find_element(*self.pwd_loc).send_keys(pwd)
        
    def login(self):
        self.find_element(*self.login_loc).click()
    
def user_login(driver,username,pwd):
    login_page = LoginPage(driver)
    login_page.open()
    driver.find_element_by_partial_link_text("登录").click()
    time.sleep(3)
    driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
    time.sleep(3)
    login_page.type_username(username)
    login_page.type_pwd(pwd)
    login_page.login()
    
def main():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        username = "15088558058"
        pwd = "fc678268"
        user_login(driver,username,pwd)
        time.sleep(3)
        text = driver.find_element_by_id("").text
        print(text)
        assert (text == ""),"用户名不匹配，登录失败"
    finally:
        driver.close()

if __name__ == '__main__':
        main()
    