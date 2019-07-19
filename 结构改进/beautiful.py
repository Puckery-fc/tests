# -*- coding: utf-8 -*-
# File  : beautiful.py
# Date  : 2018/12/28

import unittest,os,time
from BeautifulReport import BeautifulReport
from myemail import Email


if __name__ == "__main__":
    
    suite = unittest.defaultTestLoader.discover("H:\\fc\\test_case",pattern = "test*.py",top_level_dir = None)
    BeautifulReport(suite).report(filename = "测试报告",description = "搜索",log_path = "H:\\fc\\TestReport")
    
    
    email_host = "smtp.qq.com"
    host_port = 465
    from_addr = "691618966@qq.com"
    pwd = "ytrrkmtghhckbegf"
    # 获取最新生成的测试报告附件
    result_dir = r'H:\\fc\\TestReport'
    lists = os.listdir(result_dir)
    lists.sort()
    file_new = os.path.join(lists[-1])
    source_path = result_dir + '\\' + file_new
    to_addr_list = ["15088558058@qq.com,691618966@qq.com"]
    email_content = "t_report"
    email_content_html = "tttt"
    email_subject = "t_report"
    email_from = "12332"
    part_name = "test.html"
    email_obj = Email.get_email_obj(email_subject, email_from, to_addr_list)
    Email.attach_content(email_obj, email_content)
    Email.attach_part(email_obj, source_path, part_name)
    Email.send_email(email_obj, email_host, host_port, from_addr, pwd, to_addr_list)
    exit()

    # unittest.defaultTestLoader.discover(".", pattern = "*tests.py",
    #                                     top_level_dir = None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    # BeautifulReport(suite_tests).report(filename = '百度测试报告', description = '搜索测试',
    #                                     log_path = '.')  # log_path='.'把report放到当前目录下