'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 下拉框.py
# @Author: fangcheng
# @Date  : 2018/8/15
'''
# #接受警告信息
# alert = driver.switch_to_alert()
# alert.accept()
# #得到文本信息打印
# alert = driver.switch_to_alert()
# print alert.text()
# #取消对话框（如果有的话）
# alert = driver.switch_to_alert()
# alert.dismiss()
# #输入值
# alert = driver.switch_to_alert()
# alert.send_keys(“xxx”)



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os,time

d = webdriver.Firefox()
url = ("https://www.baidu.com/")
d.get(url)
ele =d.find_element_by_link_text("设置")
ActionChains(d).move_to_element(ele).perform()
d.find_element_by_link_text("搜索设置").click()
time.sleep(3)
ele1 = d.find_element_by_name("NR").find_element_by_css_selector("#nr > option:nth-child(2)").click()
time.sleep(3)
ele2 = d.find_element_by_id("se-setting-5").find_element_by_id("sh_1").click()

d.find_element_by_class_name("prefpanelgo").click()

# alert的使用
d.switch_to_alert().accept()

d.quit()




