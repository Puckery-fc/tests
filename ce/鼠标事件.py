'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 鼠标事件.py
# @Author: fangcheng
# @Date  : 2018/8/14
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 定位到要右击的元素
qqq = driver.find_element_by_xpath("xxxx")
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(qqq).perform()

#定位到要双击的元素
qqq =driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(qqq).perform()

#定位元素的原位置
element = driver.find_element_by_name("source")
#定位元素要移动到的目标位置
target = driver.find_element_by_name("target")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()
