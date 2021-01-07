#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_email.py
# @Time      :2020/7/10 17:55
# @Author    :麻花

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#邮件发送的用户名和密码常识: 第三方授权码
_user =""
_pwd = ""

now = time. strftime('%Y-%m-%d_%H_%M_%S')#获取时间

class sendEmail:
    def send_email(self,email_to,filepath):
        #email_to收件方
        #filepath你要发送附件的地址
        #如名字所示Multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = now +"麻花的测试报告"
        msg["From"] = _user
        msg["To"] = email_to

        # ---这是文字部分---
        part = MIMEText("这次是自动化测试结果，请查收! ")
        msg.attach(part)

        #---这是附件部分---
        part = MIMEApplication(open(filepath,'rb').read())
        part.addheader('Content-Disposition','attachment',filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.qq.com",timeout=30)#连接smtp邮件服务器,端口默认是25
        s.login(_user, _pwd)# 登陆服务器
        s.sendmail(_user, email_to, msg.as_string())#发送邮件
        s.close()



