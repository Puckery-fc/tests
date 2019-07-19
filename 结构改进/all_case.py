'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : all_case.py
# @Author: fangcheng
# @Date  : 2018/8/16
'''
import unittest, sys

# 把 test_case 目录添加到 path 下
sys.path.append("\test_case")
# 导入 test_case 目录下的所有文件
from test_case import *
import HTMLTestReport


# 将用例组装数组
def caselist():
    alltestnames = [
        test_baidu.BaiduTest,
        test_youdao.YoudaoTest,
        test_zhihu.zhihuTest,
    ]
    print("sucess read case list")
    return alltestnames

# 创建测试套件
suit = unittest.TestSuite()
# 循环读取数组中的用例
for test in alltestnames:
    suit.addTest(unittest.makeSuite(test))
#定义个报告存放路径，支持相对路径

filename = "H:\\fc\\TestReport\\result2220.html"
fp = open(filename, 'wb')
runner = HTMLTestReport.HTMLTestRunner(
    stream=fp,
    title="TestReport"
)
runner.run(suit)
