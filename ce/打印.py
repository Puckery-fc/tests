'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 11.py
# @Author: fangcheng
# @Date  : 2018/8/14
'''
from selenium import webdriver
b = webdriver.Firefox()
url = "https://www.baidu.com"
print(url)
b.get(url)
title =b.title
url =b.current_url

b.implicitly_wait(30)
#  b.find_element_by_link_text("贴吧").click()
b.find_element_by_partial_link_text("贴").click()
print(b.title)
print(title)
print(url)
b.quit()