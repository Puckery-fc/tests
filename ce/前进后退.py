'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 前进后退.py
# @Author: fangcheng
# @Date  : 2018/8/14
'''
from selenium import webdriver
import time

b = webdriver.Firefox()
url = "https://www.baidu.com"
print(b.title)
print(url)
b.get(url)
time.sleep(3)

url2 = "http://news.baidu.com/"
print(b.title)
print(url2)
b.get(url2)
time.sleep(3)

print(url)
b.back()
print(b.title)
time.sleep(2)
print(url2)
b.forward()
time.sleep(2)
b.quit()
