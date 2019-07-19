# -*- coding: utf-8 -*-
# File  : handle.py
# Date  : 2018/11/13
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
ele1 = browser.find_element_by_id('kw').send_keys('三星S10')
ele2 = browser.find_element_by_id('su').click()
time.sleep(2)
ele3 = browser.find_element_by_xpath('//*[@id="1"]/div/div[5]/a').click()
time.sleep(2)

handles = browser.window_handles
for handle in handles:
    if handle != browser.current_window_handle:
        browser.switch_to.window(handle)

#
# now_handle = browser.current_window_handle   #获取当前窗口
# all_handle = browser.window_handles     #获取所有窗口
#
# for handle in all_handle:
#     if handle != now_handle:
#         browser.switch_to.window(handle)