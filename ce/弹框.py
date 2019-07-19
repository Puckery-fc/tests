# -*- coding: utf-8 -*-
# File  : 弹框.py
# Date  : 2019/5/7

from selenium import webdriver
import unittest,time

class alert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://puckery.ys168.com/"
        self.driver.implicitly_wait(30)
        
    def test_alert(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("buyh").find_element_by_css_selector("#buyh > input:nth-child(2)").click()
        print(55555)
        time.sleep(3)
        driver.switch_to_frame("F_ck_zxlb_html")
        driver.find_element_by_css_selector("body > div:nth-child(2) > input:nth-child(1)").click()
        print(3333)
        time.sleep(6)
        driver.switch_to_default_content()
        
if __name__ == '__main__':
    unittest.main()