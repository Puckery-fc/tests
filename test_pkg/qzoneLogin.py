# -*- coding: utf-8 -*-
# File  : qzoneLogin.py
# Date  : 2019/5/29


# 未完成
# 未完成
# 未完成
# 未完成
from selenium import webdriver
import time,os

def openBrowser():
    browser = webdriver.Chrome()
    return browser
def openUrl(browser,url):
    browser.get(url)
    browser.maximize_window()
    
def findElement(browser,self):
    time.sleep(3)
    base_url = browser.find_element_by_partial_link_text(self["登录"]).click()
    base_page = browser.find_element_by_id(self["TANGRAM__PSP_10__footerULoginBtn"]).click()
    user_page = browser.find_element_by_id(self["TANGRAM__PSP_10__userName"])
    pwd_page = browser.find_element_by_id(self["TANGRAM__PSP_10__password"])
    login_page = browser.find_element_by_id(self["TANGRAM__PSP_10__submit"])
    return base_url,base_page,user_page,pwd_page,login_page

def checkResult(browser,errId):
    time.sleep(2)
    try:
        result = False
        error = browser.find_element_by_id(errId)
        print("登录失败")
        print(error.txt)
    except Exception:
        result = True
        print("登陆成功")
    return result

def LoginOut(browser,loginText):
    loginOut = browser.find_element_by_partial_link_text(loginText).click()
    return loginOut

if __name__ == '__main__':
    LOGIN = {"url":"https://www.baidu.com","text":"登录",}
