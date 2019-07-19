'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 读取文件参数化.py
# @Author: fangcheng
# @Date  : 2018/8/15
'''
from selenium import webdriver
import os, time

# open 方法左以只读方式（r）打开本地的 data.txt 文件，readlines方法是逐行的读取文件内容。
# 通过 for 循环，serch 可以每次获取到文件中的一行数据，在定位到百度的输入框后，
# 将数据传入 send_keys(serch)。这样通过循环调用，直到文件的中的所有内容全被读取

source = open("H:\\fc\\222.txt", "r")
values = source.readlines()
source.close()

# 执行循环

for serch in values:
    b = webdriver.Firefox()
    b.get("http://www.baidu.com")
    b.find_element_by_id("kw").send_keys(serch)
    b.find_element_by_id("su").click()
    time.sleep(3)
    b.quit()
