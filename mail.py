# -*- coding: utf-8 -*-
from aifc import Error
from email.mime.text import MIMEText
from email.header import Header
from smtplib import *
import Global

def SendEmail(content):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = Global.get_value('qq')
    # pwd为qq邮箱的授权码
    pwd = Global.get_value('mailpwd')
    # 发件人的邮箱
    sender_qq_mail = Global.get_value('qq')+'@qq.com'
    # 收件人邮箱
    receiver = Global.get_value('mail')
    # 邮件的正文内容
    mail_content = content['content']

    # 邮件标题
    mail_title = content['title']

    # ssl登录

    try:
        smtp = SMTP_SSL(host_server)
        smtp.login(sender_qq, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
    except Error as e:
        print(e)