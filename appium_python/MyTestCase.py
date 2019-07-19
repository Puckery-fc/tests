# -*- coding: utf-8 -*-
# File  : kk.py
# Date  : 2019/5/23

from appium import webdriver
import time,selenium,unittest,pkg_resources
from  appium.webdriver.common.touch_action import TouchAction

class MyTestCase(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['appPackage'] = 'com.bohaoo.guanwan'
        desired_caps['appActivity'] = 'com.bohaoo.guanwan.AppActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    def test_sth(self):
        print('test_something click ------ ')
        time.sleep(2)
        TouchAction(self).perform(x = 447, y = 171).release().perform()

        
    # @classmethod
    # def tearDown(self):
    #     time.sleep(5)
    #     print('tearDown ------ ')
    #     self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
        
        
    # desired_caps = {
    #     'platformName':'Android',
    #     'deviceName':'d96643e',
    #     'platformVersion':'8.1.0',
    #     'appPackage':'com.bohaoo.guanwan',
    #     'appActivity':'com.bohaoo.guanwan.AppActivity'
    #    }
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
