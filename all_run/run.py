# -*- coding: utf-8 -*-
# File  : runner.py
# Date  : 2019/5/21
import sys, unittest, HTMLTestReport, time, os
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    allcase = 'H:\\fc\\test_pkg'
    suite = unittest.defaultTestLoader.discover(allcase,
                                                pattern = "test_*.py",
                                                top_level_dir = None)
    BeautifulReport(suite).report(filename = "测试报告",
                                  description = "搜索",
                                  log_path = "H:\\fc\TestReport")
    