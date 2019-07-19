# -*- coding: utf-8 -*-
# File  : eg6.py
# Date  : 2019/5/22

import unittest,doctest,os
import test_pkg.test_wy_obj,test_pkg.test_qzone,test_pkg.test_Qmail
import HTMLTestReport

suite = doctest.DocTestSuite()
print(suite)
suite.addTest(unittest.makeSuite(test_pkg.test_Qmail.main()))
# suite.addTest(unittest.makeSuite(test_pkg.test_wy_obj.main()))
# suite.addTest(unittest.makeSuite(test_pkg.test_qzone.qzone()))

