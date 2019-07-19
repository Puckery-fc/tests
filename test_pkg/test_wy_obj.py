# -*- coding: utf-8 -*-
# File  : obj.py
# Date  : 2019/5/5


from selenium import webdriver
from selenium.webdriver.common.by import By
from BeautifulReport import BeautifulReport
from time import sleep
import os,time,unittest

class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'https://mail.163.com'
    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30


    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self,url):
        url = self.base_url + url
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(),'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

class LoginPage(Page):
    """
    163邮箱登录页面模型
    """
    url = '/'
    #定位器
    username_loc = (By.NAME,'email')
    password_loc = (By.NAME,'password')
    submit_loc = (By.ID,'dologin')

    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def submit(self):
        self.find_element(*self.submit_loc).click()

def test_user_login(driver,username,password):
    """
    测试获取的用户名/密码是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open()
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to_frame(iframe)
    # driver.switch_to.frame("x-URS-iframe")
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    
def main():
      try:
        driver = webdriver.Chrome()
        username = '15088558058'
        password = 'fc678268'
        test_user_login(driver, username, password)
        sleep(3)
        driver.switch_to.default_content()
        text = driver.find_element_by_xpath("//*[@id='spnUid']").text
        assert (text == "150****8058@163.com"),"用户名不匹配，登录失败"
      finally:
          driver.close()

if __name__=='__main__':
    main()
    # try:
    #     driver = webdriver.Firefox()
    #     username = '15088558058@163.com'
    #     password = 'fc678268'
    #     test_user_login(driver,username,password)
    #     sleep(3)
    #     driver.switch_to.default_content()
    #     text = driver.find_element_by_xpath("//span[@id='spnUid']").text
    #     assert(text == 'username@163.com'),'用户名称不匹配，登录失败!'
    # finally:
    #     #关闭浏览器窗口

    suite = unittest.defaultTestLoader.discover("H:\\fc\\test_pkg", pattern = "wy_obj.py", top_level_dir = None)
    BeautifulReport(suite).report(filename = "测试报告",
                                      description = "login",
                                      log_path = "H:\\fc\\TestReport")
    
        