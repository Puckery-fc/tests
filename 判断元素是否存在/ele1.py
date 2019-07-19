# -*- coding: utf-8 -*-
# File  : ele1.py
# Date  : 2018/12/26

def is_element_exsist(driver,locator):
    
    # 判断元素是否存在, 存在返回True, 不存返回False
    # :param
    # locator: locator为元组类型，如("id", "yoyo")
    # :return: bool值，True or False

    try:
        driver.find_element(*locator)
        return True
    except Exception as msg:
        print("元素%s找不到：%s" % (locator, msg))
        return  False
if __name__ == '__main__':
    loc1 = ("id","yoyo") #元素1
    print(is_element_exsist(driver,loc1))
        