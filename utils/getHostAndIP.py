# -*- coding: UTF-8 -*- 
'''
utils.getIPAdderss is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2017, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import GetBanguHome
import socket

def getHostNameIP():
    host_name = socket.getfqdn(socket.gethostname())
    ip_address = socket.gethostbyname(host_name)
    return (host_name, ip_address)

def getHostName():
    return getHostNameIP()[0]

def getIP():
    return getHostNameIP()[1]

if __name__ == "__main__":
    print getHostNameIP()
    print getIP()
    print getHostName()