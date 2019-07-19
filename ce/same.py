# -*- coding: utf-8 -*-
# File  : same.py
# Date  : 2018/11/29
from selenium import webdriver
import time
def startBrowser(name):
    """
    打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
        if name == "firefox" or name == "Firefox":
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            return driver
        elif name == "chrome" or name == "Chrome":
            print("start browser name :Chrome")
            driver = webdriver.Chrome()
            return driver
        else:
            print("Not found this browser,You can use 'firefox'")
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

def run_case(name):
    driver = startBrowser(name)
    driver.get("http://www.baidu.com")
    time.sleep(3)
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    names = ["chrome", "Firefox"]
    for i in names:
        run_case(i)