# -*- coding: UTF-8 -*- 
'''
API code from https://pushover.net/. 

Controller.Pushover is a part of the project bangu.
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

from utils import pushover_sounds
import urllib, random
import json
    
class Pushover:
    def __init__(self, token = None, user = None, sound = None):
        self.token = token if token else 'ae9qi675k39yruy7o1rnnwgr7k4yx9'
        self.user = user if user else 'udso6ennzjquetj9aiv9t3vkvgw2to'
        self.sound = sound if sound else pushover_sounds[random.randint(0, len(pushover_sounds) - 1)]
        try:
            import httplib
            self.conn = httplib.HTTPSConnection("api.pushover.net:443")
        except:
            import http.client
            self.conn = http.client.HTTPSConnection("api.pushover.net:443")
            
    def notify(self, text):
        try:
            self.conn.request("POST", "/1/messages.json",
                  urllib.urlencode({
                    "token": self.token,
                    "user": self.user,
                    "message": text.encode("utf8"),
                    "sound": self.sound,
                  }), { "Content-type": "application/x-www-form-urlencoded" })
        except Exception, e:
            print e
            pass

if __name__ == "__main__":
    Pushover().notify("2017-01-08-16:48:26")
        