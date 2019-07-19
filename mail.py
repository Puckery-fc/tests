'''
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@time: 2018/8/3 11:51
@desc:
'''
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.qq.com'
from_mail = "691618966@qq.com"
# 服务授权码
mail_pass = "ytrrkmtghhckbegf"
# mail = input("请输入邮箱：")
# to_mail = n
to_mail = "15088558058@qq.com"
msg = MIMEMultipart()
msg["From"] = from_mail
msg["To"] = to_mail
msg["Subject"] = Header('自动化测试报告', 'utf-8').encode()

TextPart = MIMEText(u"邮件发送测试")
msg.attach(TextPart)

xlsxPart = MIMEApplication(open(r'F:\旧包\7月份\双扣\2.xlsx', 'rb').read())
xlsxPart.add_header('Content-Disposition', 'attachment', filename="2.xlsx")
msg.attach(xlsxPart)

try:
    s = smtplib.SMTP_SSL(smtp_server, 465)
    s.connect(smtp_server)
    s.login(from_mail, mail_pass)
    s.sendmail(from_mail, to_mail, msg.as_string())
    s.quit()
    print(u'恭喜发送邮件成功')
except smtplib.SMTPException as e:
    print ("Error: %s") % e
