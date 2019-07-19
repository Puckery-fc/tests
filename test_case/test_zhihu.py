'''
Created on 2018年6月20日

@author: Administrator
'''
from selenium import  webdriver
import unittest,time
#import pdb 
#import HTMLTestRunner 

class zhihuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.zhihu.com"
        
    def test_zhihu(self):
        u'知乎测试'
         
#        pdb.set_trace()
        driver = self.driver
        driver.get(self.base_url +"/")
        driver.find_element_by_class_name("Input").clear()
        
        try:
            driver.find_element_by_class_name("Input").send_keys("python")
        except:
            driver.get_screenshot_as_file("H:\selenium_use_case\error_png\kw.png")
            
        driver.find_element_by_xpath("//*[@id='root']/div/div[2]/header/div[1]/div[1]/div/form/div/div/div/div/button").click()
        time.sleep(3)

        
    def tearDown(self):
        self.driver.quit()
                
                
if __name__=='_main_':
    
        unittest.main()