'''
Created on 2018年8月1日

@author: Administrator
'''
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders

class Email():
    def get_email_obj(email_subject,email_from,to_addr_list):

        # 构造邮件对象，并设置邮件主题、发件人、收件人，最后返回邮件对象
        # email_subject: 邮件主题
        # email_from: 发件人
        # to_addr_list: 收件人列表
        # return:邮件对象email_obj
        # 构造 MIMEMultipart 对象做为根容器

        email_obj = MIMEMultipart()
        email_to =','.join(to_addr_list)
        email_obj['Subject']=Header(email_subject,'utf-8')
        email_obj['From']= Header(email_from,'utf-8')
        email_obj['To']=Header(email_to,'utf-8')
        return email_obj
    def attach_content(email_obj,email_content,content_type='plain',charset='utf-8'):

        # 创建邮件正文，并将其附加到跟容器：邮件正文可以是纯文本，也可以是HTML（为HTML时，需设置content_type值为
        # 'html'）
        # email_obj: 邮件对象
        # email_content: 邮件正文内容
        # content_type: 邮件内容格式'plain'、'html'..，默认为纯文本格式'plain'
        # charset: 编码格式，默认为utf - 8

        content = MIMEText(email_content,content_type,charset)
        email_obj.attach(content)

    def attach_part(email_obj,source_path,part_name):
        # source_path: 附件源文件路径
        # part_name: 附件名

        part = MIMEBase('application', 'octet-stream')  # 'octet-stream': binary data   创建附件对象
        part.set_payload(open(source_path, 'rb').read())  # 将附件源文件加载到附件对象
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % part_name)  # 给附件添加头文件
        email_obj.attach(part)  # 将附件附加到根容器

    def send_email(email_obj, email_host, host_port, from_addr, pwd, to_addr_list):

        # email_obj: 邮件对象
        # email_host: SMTP服务器主机
        # host_port: SMTP服务端口号
        # from_addr: 发件地址
        # pwd: 发件地址的授权码，而非密码
        # to_addr_list: 收件地址

        try:

                # import smtplib
                # smtp_obj = smtplib.SMTP([host[, port[, local_hostname]]] )
                    # host: SMTP服务器主机。
                    # port: SMTP服务端口号，一般情况下SMTP端口号为25。
                # smtp_obj = smtplib.SMTP('smtp.qq.com', 25)
            print (email_host,host_port)
            smtp_obj = smtplib.SMTP_SSL(email_host, host_port)  # 连接 smtp 邮件服务器
            smtp_obj.connect(email_host)
            print (from_addr,pwd)
            smtp_obj.login(from_addr, pwd)
            print (email_obj.as_string())
            print (from_addr,to_addr_list)
            smtp_obj.sendmail(from_addr, to_addr_list, email_obj.as_string())  # 发送邮件：email_obj.as_string()：发送的信息
            smtp_obj.quit()  # 关闭连接
            print("发送成功！")
            return True
        except smtplib.SMTPException as e:
            print (e)
            print("发送失败！")
            return False