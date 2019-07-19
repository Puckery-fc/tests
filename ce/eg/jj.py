# -*- coding: utf-8 -*-
# File  : jj.py
# Date  : 2018/11/19
import unittest
from xx import count

class testCount(unittest.TestCase):    #需要继承unittest里的TestCase
    def setUp(self):  #准备环境,连接数据
        self.obj = count()
        #print('call setUp')
    def tearDown(self):     #清理环境,关闭数据
        self.obj = None
        #print('call tearDown')
    def Test_add(self):
        print(self.obj.add(2, 3) == 5)
    def Test_sub(self):
        print(self.obj.sub(5, 3) == 3)

if __name__ == '__main__':
    addcountDemo = testCount('Test_add')
    addcountDemo.run()
    subcountDemo = testCount('Test_sub')
    subcountDemo.run()
