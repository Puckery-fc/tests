# -*- coding: utf-8 -*-
# File  : ll.py
# Date  : 2019/5/24

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,unittest,os



desired_caps = {
            'platformName': 'Android',
            'platformVersion':'6.0.1',
            # 'deviceName': '127.0.0.1:62001',
            'deviceName': '7b74d46b',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'noReset': 'True',
            # 'unicodeKeyboard': 'True',
            # 'resetKeyboard': 'True',
            'chromeOptions': {
            'androidProcess': 'com.tencent.mm:appbrand0'
                }
            }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_name("发现").click()
# driver.find_element_by_name("小程序").click()
# driver.find_element_by_name("X东购物").click()
# driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
# time.sleep(5)
# print(driver.page_source)