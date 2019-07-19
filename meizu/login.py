# -*- coding: utf-8 -*-
# File  : login.py
# Date  : 2019/4/28
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time,unittest

class meizu(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = "https://detail.meizu.com/item/meizu16s.html?skuId=10911&click=store_list_kw_1"

    def test_distribution(self):
        driver = self.driver
        driver.get(self.url)
        driver.maximize_window()
        

        driver.find_element_by_class_name("property-sibling").find_element_by_xpath("//*[@id='property']/div[4]/dl/dd/a[2]").click()
        driver.find_element_by_class_name("property-set").find_element_by_xpath("//*[@id='property']/div[5]/dl[2]/dd/a[2]").click()
        driver.find_element_by_class_name("property-set").find_element_by_xpath("//*[@id='property']/div[5]/dl[3]/dd/a[2]").click()
        driver.find_element_by_class_name("property-set").find_element_by_xpath("//*[@id='J_packageTab']/a[2]").click()
        driver.find_element_by_class_name("property-set").find_element_by_xpath("//*[@id='J_huabeiBody']/a[2]").click()
        driver.find_element_by_class_name("property-buy").find_element_by_class_name("vm-plus").click()
        
        time.sleep(6)
        driver.find_element_by_id("site-selector").click()
        adress = driver.find_element_by_id("site-selector").find_element_by_class_name("text")
        ActionChains(driver).move_to_element(adress).perform()
        time.sleep(3)
        # driver.find_element_by_class_name("mc").find_element_by_xpath("//*[@id='site-province-item']/ul/li[7]/a").click()
        # time.sleep(3)
        # driver.find_element_by_class_name("mc").find_element_by_xpath("//*[@id='site-city-item']/ul/li/a").click()
        # time.sleep(3)
        driver.find_element_by_class_name("mc").find_element_by_xpath("//*[@id='site-area-item']/ul/li[12]/a").click()
        time.sleep(3)
        driver.find_element_by_class_name("mc").find_element_by_xpath("//*[@id='site-town-item']/ul/li[19]/a").click()

        '''''
        adress = driver.find_element_by_css_selector("#site-selector > div.text > i")
        ActionChains(driver).move_to_element(adress).perform()
        time.sleep(3)
        '''''
        
        '''''
        adress1 = driver.find_element_by_css_selector("#JD-stock > div.mt > ul > li.curr > a > i")
        ActionChains(driver).move_to_element(adress1).perform()
        driver.find_element_by_link_text("上海").click()
        time.sleep(3)
        adress2 = driver.find_element_by_class_name("curr")
        ActionChains(driver).move_to_element(adress2).perform()
        driver.find_element_by_link_text("上海市").click()
        time.sleep(3)
        adress3 = driver.find_element_by_link_text("浦东新区").click()
        '''''
        
        
        
    
if __name__ == "__main__":
    unittest.main()
        