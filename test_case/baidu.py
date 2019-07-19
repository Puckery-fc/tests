# -*- coding: utf-8 -*-
# File  : kkkk.py
# Date  : 2018/12/4
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
import HTMLTestReport
import unittest, time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(2)
        self.driver.get('https://www.baidu.com/')
        #self.Erros = []      #定义一个空数组，方便判断测试结果

    def test_baidu(self):
        '''百度搜索测试'''
        driver = self.driver
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, 'selenium_百度搜索')

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by = how, value = what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True

    def tearDown(self):
        print('测试完毕')
        self.driver.quit()
        #self.assertEqual([], self.Erros)     #在这里用一个空数组，如果空数组等于self.Erros，则说明没有报错

    #def test_report(self):   #这里的函数名只能用test_**才会执行，因为测试用例里只能搜索test开头的函数并执行

if __name__ == '__main__':
    print('报告')
    testunnit = unittest.TestSuite()
    testunnit.addTest(BaiduTest('test_baidu'))
    now = time.strftime('%Y-%m-%d', time.gmtime())
    fp = open('C:\\Users\\user\\Desktop\\' + now + 'result.html', 'wb')
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况:')
    # runner = unittest.TextTestRunner()
    runner.run(testunnit)
    #fp.close()  # 关闭文件流，不关的话生成的报告是空的
    #unittest.main()
