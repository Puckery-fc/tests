# -*- coding: utf-8 -*-
# File  : window.py
# Date  : 2018/11/29
from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("麦德龙")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.find_element_by_partial_link_text("麦德龙官方网站").click()
driver.quit()

