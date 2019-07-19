# -*- coding: utf-8 -*-
# File  : wait.py
# Date  : 2018/11/29
from selenium import  webdriver
from selenium.webdriver.support.ui import  WebDriverWait
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#WebDriverWait()方法的使用

element = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("kw") )
element.send_keys("123")

#添加智能等待

driver.implicitly_wait(10)
driver.find_element_by_id("su").click()
#添加固定休眠时间

time.sleep(5)
