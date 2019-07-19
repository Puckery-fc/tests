# -*- coding: utf-8 -*-
# File  : unit.py
# Date  : 2018/11/29
from selenium import webdriver
import unittest, time


class baidutest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        try:
            # kwddd 是一个无法找到的元素 id
            driver.find_element_by_id("kw").send_keys("知乎")
        except:
            driver.get_screenshot_as_file("H:\selenium_use_case\error_png\kw.png")
            # 如果没有找到上面的元素就截取当前页面。
        driver.find_element_by_id("su").click()
        time.sleep(3)


'''
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()s
            alert_text = alert.text()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
                return alert_text
        finally: self.accept_next_alert = True
'''


def teardown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
