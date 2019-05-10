#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)


    # 添加附件，传送./1.rar文件
    part = MIMEApplication(open('1.rar','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="1.rar")
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()

try:
    subject = '邮件带有发送的附件'
    content = 'test'
    send_email('smtp.163.com', '****@163.com', '*****', 'sunx36ose@vip.qq.com', subject, content)
except Exception as err:
    print(err)