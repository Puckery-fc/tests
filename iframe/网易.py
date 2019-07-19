# -*- coding: utf-8 -*-
# File  : 网易.py
# Date  : 2019/4/30

from selenium import webdriver
import time,unittest,iframe

class wy(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = "https://mail.163.com/"
        
    def test_lg(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("loginBlock").click()
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to_frame(iframe)
        driver.find_element_by_name("email").send_keys("15088558058")
        driver.find_element_by_name("password").send_keys("fc678268")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='dologin']").click()
        driver.switch_to_default_content()
        # windows = driver.window_handles
        # print(windows)
        # driver.switch_to_window(windows[-1])
        time.sleep(2)
        driver.find_element_by_id("_mail_component_132_132").find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[3]/ul/li[1]/div[1]/b[1]").click()
        

        # window_1 = driver.current_window_handle
        # windows = driver.window_handles
        # for current_window in windows:
        #     if current_window != window_1:
        #         driver.switch_to_window(current_window)
        #         time.sleep(3)

    # def tearDown(self):
    #     self.driver.quit()

    
        
        
if __name__ == "__main__":
    unittest.main()
    
    