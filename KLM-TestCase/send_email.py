#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 15:38
# @Author  : WangDonghe
# @Site    : 
# @File    : send_email.py
# @Software: PyCharm

import unittest
import HTMLTestRunner
import os ,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from all_case import report

def send_email(file_new):
    mail_from = '294598473@qq.com'
    mail_to = ['wangdonghe@klm123.com']
    with open(file_new,'rb') as f:
        mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject']=u'接口测试报告'+time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtpsever = 'smtp.qq.com'
    username = '294598473@qq.com'
    password = 'lsbsazrjpdqnbhcg'
    smtp = smtplib.SMTP_SSL(smtpsever,465)
    smtp.connect('smtp.qq.com')
    smtp.login(username,password)
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print('email has send out !')

def sendreport():
    reprort_dir = 'E:\PycharmProjects\\untitled\\report\\'
    lists = os.listdir(reprort_dir)
    lists.sort(
        key=lambda fn: os.path.getmtime(reprort_dir  + fn) if not os.path.isdir(reprort_dir + fn) else 0)
    print(lists[-1])
    file_new = os.path.join(reprort_dir, lists[-1])
    print(file_new)
    send_email(file_new)
report()
sendreport()