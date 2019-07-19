# -*- coding: utf-8 -*-
# File  : runner.py
# Date  : 2019/5/21


import sys,unittest,HTMLTestReport,time,os

allcase = 'H:\\fc\\test_case'

def createSuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(allcase,
                                                   pattern = "test_*.py",
                                                   top_level_dir = None)
    for suite in discover:
        for case in suite:
            testunit.addTests(case)
            print(testunit)
    return testunit
if __name__ == '__main__':
      
      allcasenames = createSuite()
      now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
      filename='H:\\fc\\TestReport'+now+"test_all.html"
      fp=open(filename,'wb')
      runner = HTMLTestReport.HTMLTestRunner(stream = fp,
                                       title = "",
                                       description = "")
      runner.run(allcasenames)
      fp.close()