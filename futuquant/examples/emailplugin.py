# -*- coding: utf-8 -*-
"""
    邮件提醒功能
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailNotification(object):
    """邮件提醒类"""
    sender = 'your sender email address'
    password = 'your password'
    smtpserver = 'your smtp server,such as smtp.163.com'
    enable = False

    @staticmethod
    def set_enable(enable=False):
        EmailNotification.enable = enable

    @staticmethod
    def is_enable():
        return EmailNotification.enable

    @staticmethod
    def send_email(receiver, subject, words):
        if not EmailNotification.is_enable():
            return
        try:
            msg = MIMEText(words, 'plain', 'utf-8')      # 中文需参数‘utf-8'，单字节字符不需要
            msg['Subject'] = Header(subject, 'utf-8')    # 邮件标题
            msg['from'] = EmailNotification.sender       # 发信人地址
            msg['to'] = receiver                         # 收信人地址

            smtp = smtplib.SMTP()
            smtp.connect(EmailNotification.smtpserver)
            smtp.login(EmailNotification.sender, EmailNotification.password)
            smtp.sendmail(EmailNotification.sender, receiver,
                          msg.as_string())               # 这行代码解决的下方554的错误
            smtp.quit()
            print("邮件发送成功!")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    pass
