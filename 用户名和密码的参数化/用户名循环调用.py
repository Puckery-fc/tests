'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 用户名.py
# @Author: fangcheng
# @Date  : 2018/8/16
'''
from selenium import webdriver
import os, time
from selenium.webdriver.common.keys import Keys
import fun

# 循环调用字典里的用户名密码，分别赋值给 k,v
for k, v in fun.zidian().items():
    print(k,v)
    b = webdriver.Firefox()
    url = ("http://www.sohu.com/")
    b.get(url)
    time.sleep(9)
    b.find_element_by_link_text("登录狐友").click()
    time.sleep(3)
    b.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]").click()
    b.find_element_by_class_name("user-input").clear()
    b.find_element_by_class_name("user-input").send_keys(k)
    time.sleep(3)
    b.find_element_by_class_name("user-input").send_keys(Keys.TAB)
    time.sleep(3)
    b.find_element_by_class_name("password-input").clear()
    b.find_element_by_class_name("password-input").send_keys(v)

    b.find_element_by_class_name("password-input").send_keys(Keys.ENTER)
    b.close()
