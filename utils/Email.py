# -*- coding: UTF-8 -*- 
'''
utils.Email is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import GetBanguHome
import smtplib, email
from utils.ReadConfig import configurations
import os

uniformMsg = """<h4>您好，</h4>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;非常感谢您对bangu项目的关注，这是一个基于树莓派实现的智能硬件项目，使用python语言开发。
    <p>&nbsp;&nbsp;&nbsp;&nbsp;获得最新bangu项目的信息，欢迎您访问我的github
    <p>&nbsp;&nbsp;&nbsp;&nbsp;https://github.com/wangqingbaidu/bangu
    <p>&nbsp;&nbsp;&nbsp;&nbsp;关于我的最新动态您可以访问我的blog
    <p>&nbsp;&nbsp;&nbsp;&nbsp;http://www.wangqingbaidu.cn/
    <p>
    <p>
    <h4>祝好！</h4>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;哒溜君(wangqingbaidu)
    """

class Email:
    def __init__(self, cfg = configurations.get_email_settings()):
        self.__username = cfg['username']
        self.__password = cfg['password']
        self.__server = cfg['smtp']
        self.__smtp = smtplib.SMTP()
        self.__smtp.connect(self.__server)
        self.__smtp.login(self.__username, self.__password)
        
    def __attach_file(self, filename=None):
        contype = 'application/octet-stream'  
        maintype, subtype = contype.split('/', 1)
        file_msg = None
        if filename and os.path.exists(filename):
            data = open(filename, 'rb')  
            file_msg = email.MIMEBase.MIMEBase(maintype, subtype)  
            file_msg.set_payload(data.read())
            email.Encoders.encode_base64(file_msg)            
            basename = os.path.basename(filename)  
            file_msg.add_header('Content-Disposition', 'attachment', filename = basename)  
            
            data.close()
        return file_msg  
            
    def send(self, dest, subject, text=None, filename=None):
        dest_list = []
        if type(dest) == str:
            dest_list.append(dest)
        elif type(dest) == list:
            dest_list = dest
            
        if not dest_list:
            return
        
        if not text:
            text = uniformMsg
        
        file_msg = self.__attach_file(filename)
        for d in dest_list:
            msg = email.MIMEMultipart.MIMEMultipart()  
            if file_msg:
                msg.attach(file_msg) 
            text_msg = email.MIMEText.MIMEText(text, 'html', 'utf-8')
            msg.attach(text_msg)
            
            msg['from'] = 'ibangu@yeah.net'
            msg['Subject'] = subject if subject else 'from %s' %msg['from']
            msg['to'] = d
            self.__smtp.sendmail(self.__username, d, msg.as_string())

    def __del__(self):
        self.__smtp.quit()
        
if __name__ == '__main__':
    e = Email()
    e.send(['zhangzhiwei@ict.ac.cn', '564326047@qq.com'], '', '', filename='Email.py')