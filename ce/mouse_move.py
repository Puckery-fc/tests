# -*- coding: utf-8 -*-
# File  : mouse_move.py
# Date  : 2018/11/29
from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.gov.cn/")
time.sleep(2)
ele = driver.find_element_by_link_text("国务院")
webdriver.ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
ele1 = driver.find_element_by_xpath("//*[@id='mainlevel_02']/ul/li[1]/a")
ele1.click()
time.sleep(2)