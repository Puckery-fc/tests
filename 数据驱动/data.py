# -*- coding: utf-8 -*-
# File  : data.py
# Date  : 2018/9/11
import ddt
import unittest
u"测试数据"
testData = [{"user":"java","pwd":"5466"},
            {"user":"python","pwd":"55466"},
            {"user":"selenium","pwd":"545666"},
            {"user":"php","pwd":"5466799"},
            ]
@ddt.ddt
class test(unittest.TestCase):
    def setUp(self):
        print("start")
        
    def tearDown(self):
        print("end")
        
    @ddt.data(*testData)
    def test_ddt(self,data):
        print(data)
if __name__ == "__main__":
    unittest.main()
    