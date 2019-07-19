# -*- coding: utf-8 -*-
# File  : print.py
# Date  : 2018/11/29
from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.sohu.com/")
time.sleep(7)
driver.find_element_by_link_text("登录狐友").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]").click()
time.sleep(2)
driver.find_element_by_class_name("user-input").send_keys("15088558058")
time.sleep(2)
driver.find_element_by_class_name("password-input").send_keys("fc678268")
driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[2]/input").click()
title = driver.title
print(title)