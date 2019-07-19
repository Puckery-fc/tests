# -*- coding: utf-8 -*-
# File  : ele2.py
# Date  : 2018/12/26

def is_element_exsist1(driver,locator):
    
    # 判断元素是否存在, 存在返回True, 不存返回False
    # :param
    # locator: locator为元组类型，如("id", "yoyo")
    # :return: bool值，True or False
    
    eles = driver.find_elements(*locator)
    if len(eles)< 1:
        return False
    else:
        return True
if __name__ == '__main__':
    loc1 = ("id","yoyo") #元素1
    print(is_element_exsist1(driver,loc1))
    
