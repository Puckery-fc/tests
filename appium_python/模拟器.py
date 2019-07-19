# -*- coding: utf-8 -*-
# File  : ca.py
# Date  : 2019/5/24


#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,pkg_resources


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.bohaoo.guanwan'
desired_caps['appActivity'] = 'com.bohaoo.guanwan.AppActivity'
# desired_caps['unicodeKeyboard'] = 'True'
# desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(6)
# driver.find_element_by_class_name("android.widget.TextView").click()
# time.sleep(3)

TouchAction(driver).perform(ล็อกอินบัญชีนักเที่ยว).release().perform()
# driver.find_element_by_name("ล็อกอินบัญชีนักเที่ยว").click()
# driver.find_element_by_name("9").click()


# driver.quit()