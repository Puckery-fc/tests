# -*- coding: utf-8 -*-
# File  : qzone.py
# Date  : 2019/5/5


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Page(object):
    
    login_url = "https://i.qq.com/"
    
    def __init__(self,base_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = base_driver
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
    url = '/'
    # account_loc = (By.ID,'switcher_plogin')
    username_loc = (By.ID,'u')
    password_loc = (By.ID,'p')
    submit_loc = (By.ID,'login_button')
    
    # def account(self):
    #     self.find_element(*self.account_loc).click()
        
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
        
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
        
    def submit(self):
        self.find_element(*self.submit_loc).click()
        
def test_user_login(driver,username,password):
        login_page = LoginPage(driver)
        login_page.open()
        # iframe = driver.find_element_by_tag_name("iframe")
        # driver.switch_to_frame(iframe)
        driver.switch_to_frame("login_frame")
        driver.find_element_by_id("switcher_plogin").click()
        # login_page.account_loc()
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.submit()
        driver.switch_to_default_content()
        
def main():
    try:
        driver = webdriver.Chrome()
        username = "691618966"
        password = "fc678268"
        test_user_login(driver, username, password)
        time.sleep(3)
        # text = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/a[1]/span").text
        text = driver.find_element_by_class_name("user-home").text
        print(text)
        assert (text == "123。"),"failed"
    finally:
        driver.close()

if __name__ == '__main__':
    
        # driver = webdriver.Firefox()
        # username = "691618966"
        # password = "fc678268"
        # test_user_login(driver,username,password)
        # time.sleep(3)
        # driver.switch_to_default_content()
        # driver.close()
        #
        main()
        

        
    
        