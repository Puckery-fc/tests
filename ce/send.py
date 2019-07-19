'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : send.py
# @Author: fangcheng
# @Date  : 2018/8/10
'''
import yagmail
yag = yagmail.SMTP(user="691618966@qq.com",password="ytrrkmtghhckbegf",host="smtp.qq.com")
contents =["测试报告"]
yag.send("691618966@qq.com","subject",contents)
yag.send(["15088558058@qq.com"],"subject",contents)
yag.send("15088558058@qq.com","发送附件",contents,["F:\\旧包\\7月份\\双扣\\2.xlsx"])