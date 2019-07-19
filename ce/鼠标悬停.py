# -*- coding: utf-8 -*-
# File  : ssss.py
# Date  : 2018/11/16

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('https://www.jd.com/')

myJd = browser.find_element_by_link_text('我的京东')
time.sleep(3)
ActionChains(browser).move_to_element(myJd).perform()