'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 键盘事件.py
# @Author: fangcheng
# @Date  : 2018/8/14
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

b = webdriver.Firefox()
url = ("http://www.sohu.com/")
b.get(url)
time.sleep(9)
b.find_element_by_link_text("登录狐友").click()
time.sleep(3)
b.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]").click()
b.find_element_by_class_name("user-input").clear()
b.find_element_by_class_name("user-input").send_keys("15088558058")
time.sleep(3)
b.find_element_by_class_name("user-input").send_keys(Keys.TAB)
time.sleep(3)
b.find_element_by_class_name("password-input").clear()
b.find_element_by_class_name("password-input").send_keys("fc678268")

b.find_element_by_class_name("password-input").send_keys(Keys.ENTER)
