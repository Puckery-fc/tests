# -*- coding: utf-8 -*-
# File  : group.py
# Date  : 2019/5/30

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Page(object):
    login_url = "https://mail.qq.com"
    
    def __init__(self, base_driver, base_url = login_url):
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
    
    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    url = "/"
    username_loc = (By.ID, "u")
    password_loc = (By.ID, "p")
    login_loc = (By.ID, "login_button")
    
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)
    
    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
    
    def login(self):
        self.find_element(*self.login_loc).click()


def user_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    driver.switch_to_frame("login_frame")
    driver.find_element_by_id("switcher_plogin").click()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.login()
    driver.switch_to_default_content()
    time.sleep(3)
    driver.find_element_by_id("pp").send_keys("fangcheng")
    driver.find_element_by_id("btlogin").click()

def send(user_login,LoginPage):
    time.sleep(3)
    listkey = ["username","password"]
    i = 0
    for key in listkey:
        user_login[i].clear()
        user_login[i].send_keys(LoginPage[key])
        i = i + 1
    user_login[2].click()
print("测试")

def out(driver,loginText):
    out = driver.find_element_by_link_text(loginText).click()
    return loginText

class login(LoginPage,account):
    driver = webdriver.Firefox()
    


def main():
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        username = "691618966"
        password = "fc678268"
        user_login(driver, username, password)
        time.sleep(3)
        text = driver.find_element_by_id("useraddr").text
        print(text)
        assert (text == "15088558058@qq.com"), "用户名不匹配，登录失败"
    finally:
        driver.close()


if __name__ == "__main__":
    main()