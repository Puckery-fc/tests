'''
Created on 2018年6月19日

@author: Administrator
'''
from selenium import webdriver
import unittest, time


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "https://www.baidu.com"
        
    def test_baidu(self):
        u'百度测试'
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()

        try:
            driver.find_element_by_id("kw").send_keys("..")
        except:
            driver.get_screenshot_as_file("H:\selenium_use_case\error_png\kw.png")

        driver.find_element_by_id("su").click()
        time.sleep(3)
        
    def close_alert_and_get_its_test(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
                return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()













