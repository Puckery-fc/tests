# -*- coding: utf-8 -*-
# File  : 小米.py
# Date  : 2019/6/17
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

desired_caps = {
            'platformName': 'Android',
            'platformVersion':'7.1.1',
            'deviceName': 'dd3ede20',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'noReset': 'True',
            # 'unicodeKeyboard': 'True',
            # 'resetKeyboard': 'True',
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:appbrand4'
                }
            }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(6)

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

# 向下滑动
swipeDown(driver)
time.sleep(2)

# 点开小程序
driver.find_elements_by_id("com.tencent.mm:id/r9")[0].click()
time.sleep(4)

print(driver.contexts)

# 注意，这里是不需要切换的，别踩坑了！！！！！！
# driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
time.sleep(3)

# tap触摸右下角那个菜单坐标 [873,1654], [1080,1861]
driver.tap([(873, 1654), (1080, 1861)],  500)

# 点发红包赚赏金
driver.find_element_by_accessibility_id("发红包赚赏金").click()