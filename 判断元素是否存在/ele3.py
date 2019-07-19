# -*- coding: utf-8 -*-
# File  : ele3.py
# Date  : 2018/12/26

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def is_element_exsist2(driver,locator):
    
    # 结合WebDriverWait和expected_conditions判断元素是否存在,
    # 每间隔1秒判断一次，30
    # s超时，存在返回True, 不存返回False
    # :param
    # locator: locator为元组类型，如("id", "yoyo")
    # :return: bool值，True or False
    
    try:
        WebDriverWait(driver,30,1).until(EC.presence_of_all_elements_located(locator))
        return True
    except:
        return  False
if __name__ == "__main__":
    loc1 = ("id","yoyo") #元素1
    print(is_element_exsist2(driver,loc1))