'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : all_test.py
# @Author: fangcheng
# @Date  : 2018/8/16
'''
import unittest,doctest,os
import test_case.test_baidu, test_case.test_zhihu,test_case.test_youdao
import HTMLTestReport
from myemail import Email

suite = doctest.DocTestSuite()
print(suite)
suite.addTest(unittest.makeSuite(test_case.test_baidu.BaiduTest))
suite.addTest(unittest.makeSuite(test_case.test_zhihu.zhihuTest))
suite.addTest(unittest.makeSuite(test_case.test_youdao.YoudaoTest))


filename = "H:\\fc\\TestReport\\result21.html"
fp = open(filename, 'wb')
runner = HTMLTestReport.HTMLTestRunner(stream=fp,
                                       title='TestReport')
# runner = HTMLTestReport.HTMLTestRunner(stream=fp,
#                                        title='TestReport',description='4448')
runner.run(suite)

email_host ="smtp.qq.com"
host_port = 465
from_addr ="691618966@qq.com"
pwd ="ytrrkmtghhckbegf"
# 获取最新生成的测试报告附件
result_dir=r'H:\\fc\\TestReport'
lists = os.listdir(result_dir)
lists.sort()
file_new = os.path.join(lists[-1])
source_path= result_dir + '\\' + file_new
to_addr_list=["15088558058@qq.com,691618966@qq.com"]
email_content  = "t_report"
email_content_html ="tttt"
email_subject ="t_report"
email_from ="12332"
part_name = "test.html"
email_obj = Email.get_email_obj(email_subject,email_from,to_addr_list)
Email.attach_content(email_obj,email_content)
Email.attach_part(email_obj,source_path,part_name)
Email.send_email(email_obj,email_host,host_port,from_addr,pwd,to_addr_list)

fp.close()
