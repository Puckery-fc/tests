# -*- coding: utf-8 -*-
# File  : denglu.py
# Date  : 2018/9/7

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox()
# url = "http://www.sohu.com/"
# driver.get(url)
# time.sleep(6)
# driver.find_element("link text","登录狐友").click()

driver = webdriver.Firefox()
url = "https://www.baidu.com/"
driver.get(url)
driver.find_element("id","kw").send_keys("yoyoketang")
driver.quit()


