# -*- coding: utf-8 -*-
# File  : alert.py
# Date  : 2018/11/29
from selenium import  webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/?tn=25017023_10_dg")
time.sleep(5)
ele = driver.find_element_by_css_selector("#u1 > a[name='tj_settingicon']");
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(ele).perform()
ele1 = driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)
driver.find_element_by_link_text("保存设置").click()
time.sleep(3)
alert = driver.switch_to_alert()
#alert.accept()

#print(alert.text)

alert.dismiss()
driver.quit()

