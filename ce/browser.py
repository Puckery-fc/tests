# -*- coding: utf-8 -*-
# File  : browser.py
# Date  : 2018/11/29
from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#搜索
driver.find_element_by_id("kw").send_keys("123")
driver.find_element_by_id("su").click()
time.sleep(3)

#将页面滚动条拖到底部

js = "var q = document.documentElement.scrollTop = 10000"
driver.execute_script(js)
time.sleep(2)

#将滚动条拖到页面顶部

js = "var q = document.documentElement.scrollTop = 0"
driver.execute_script(js)
time.sleep(3)

driver.quit()