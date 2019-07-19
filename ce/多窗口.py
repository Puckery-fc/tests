# -*- coding: utf-8 -*-
# File  : 多窗口.py
# Date  : 2019/5/27
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_name("tj_trnews").click()
time.sleep(2)
driver.find_element_by_partial_link_text("习近平在红土地上这样谈“心”").click()
time.sleep(3)
windows = driver.window_handles
print(windows)
driver.switch_to_window(windows[-1])
time.sleep(3)
driver.find_element_by_class_name("headmenu").click()
# driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/a").click()
driver.quit()
