'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cookie.py
# @Author: fangcheng
# @Date  : 2018/8/15
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
'''
# d = webdriver.Firefox()
# url = "http://www.youdao.com/"
# d.get(url)
# 
# # 所有cookie信息
# # cookie = d.get_cookies()
# # print(cookie)
# 
# 
# #向 cookie 的 name 和 value 添加会话信息。
# d.add_cookie({'name':'key-aaaa','value':'bbbbb'})
# 
# #遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
# for cookie in d.get_cookies():
#     print (cookie['name'],cookie['value'])
# 
# #下面可以通过两种方式删除 cookie# 删除一个特定的 cookie
# d.delete_cookie("CookieName")
# 
# #删除所有 cookie
# d.delete_all_cookies()
# time.sleep(3)
# d.quit()
'''
b = webdriver.Firefox()
url = ("http://www.sohu.com/")
b.get(url)
b.maximize_window()
time.sleep(9)
b.find_element_by_link_text("登录狐友").click()
time.sleep(3)
b.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]").click()
b.find_element_by_class_name("user-input").clear()
b.find_element_by_class_name("user-input").send_keys("15088558058")
time.sleep(3)
b.find_element_by_class_name("user-input").send_keys(Keys.TAB)
time.sleep(3)
b.find_element_by_class_name("password-input").clear()
b.find_element_by_class_name("password-input").send_keys("fc678268")
time.sleep(2)
b.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/span").click()
time.sleep(2)
b.find_element_by_class_name("login-bn").click()

#获取 cookie 信息并打印
cookie = b.get_cookies()
print(cookie)
time.sleep(2)
b.close()

