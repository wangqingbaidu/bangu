# -*- coding: UTF-8 -*- 
'''
View.Hardware.Audio is a part of the project bangu.
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

import urllib2, urllib, json, subprocess
from Model import model, ModelDB
import datetime
class Audio:
    def __init__(self, model = None):
        if not model:
            self.__db = ModelDB()
        else:
            self.__db = model
    
    def getAudioAccessToken(self):        
        key = '24.7fdd91428b28017345669368767bcd27.2592000.1485051599.282335-6828205'
        try:
            key = self.db.get_latest_audio_token()
        except:            
            log = {}
            log['name'] = 'Audio.getAudioAccessToken'
            log['log'] = 'Get aduio access token error, using default key %' %key
            log['datetime'] = datetime.now()
            self.__db.insert_errorlog(log)
        return key
    
    def talk(self, msg=None):
        key = self.getAudioAccessToken()
        if msg:
            url = 'http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=A4-DB-30-FC-5A-F3&ctp=1&tok=%s' \
                %(urllib.quote(msg), key)
            
            subprocess.call(['mplayer', url], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            
if __name__ == '__main__':
    audio = Audio()
    audio.talk('Welcome to bangu.')