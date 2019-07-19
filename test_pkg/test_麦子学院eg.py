# -*- coding: utf-8 -*-
# File  : 33333.py
# Date  : 2018/11/14
# coding: UTF-8
from selenium import webdriver
import time
import os

def openBrowser():
    browser = webdriver.Firefox()
    return browser

def openUrl(browser, url):
    browser.get(url)
    browser.maximize_window()
    # time.sleep(2)
    # browser.minimize_window()

def findElement(browser,arg):
    time.sleep(2)
    loadEle = browser.find_element_by_link_text(arg['text']).click()
    accountEle = browser.find_element_by_id(arg['accountId'])
    psdEle = browser.find_element_by_id(arg['psdId'])
    loginEle = browser.find_element_by_id(arg['loginId'])
    return accountEle, psdEle, loginEle

def sendVals(ele_tuple,arg):
    time.sleep(2)
    listkey = ['username','pwd']
    i = 0
    for key in listkey:
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg[key])
        i = i + 1
    ele_tuple[2].click()

def checkResult(browser, errId):
    time.sleep(2)
    try:
        result = False
        err = browser.find_element_by_id(errId)
        print('登录失败!')
        print(err.text)
    except Exception:
        result = True
        print('登陆成功!')
    return result

def loginOut(browser, loginText):
    loginOut = browser.find_element_by_link_text(loginText).click()
    return loginOut

def login(eleDict, accountDict):
    driver = openBrowser()
    openUrl(driver, eleDict['url'])
    ele_tuple = findElement(driver, eleDict)
    for canshu in accountDict:
        sendVals(ele_tuple, canshu)
        result = checkResult(driver, eleDict['errId'])       #检查结果后，赋值给result，为下面的判断做个处理
        if result == True:     #测试登录时会有多个账号登陆，当某个账号登陆成功后，后续的账号就无法获取元素，无法继续测试，这里做个判断登陆成功的处理
            loginOut(driver, eleDict['loginText'])
            ele_tuple = findElement(driver, eleDict)
    #os.system()

if __name__ == '__main__':
    eleDict = {'url': 'http://www.maiziedu.com', 'text': '登录', 'accountId': 'id_account_l',
               'psdId': 'id_password_l', 'loginId': 'login_btn', 'errId': 'login-form-tips', 'loginText': '退出'}
    accountDict = [{'username': 'fgh@163.com', 'pwd': 'fyh'},
                   {'username': '123', 'pwd': '321'},
                   {'username': 'wyb111234@163.com', 'pwd': 'wyb3240092'},
                   {'username': '1264', 'pwd': '321'}]
    login(eleDict, accountDict)
