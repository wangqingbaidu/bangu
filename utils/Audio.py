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

import urllib, subprocess
from Model import model, ModelDB
from Controller import putErrorlog2DB
class Audio:
    def __init__(self, db = None):
        if not db:
            self.__db = ModelDB()
        else:
            self.__db = model
    
    def getAudioAccessToken(self):        
        key = '24.a30b0be4c797528a794f2da64207c665.2592000.1490496832.282335-6828205'
        try:
            key = self.__db.get_latest_audio_token()
        except Exception, e:            
            putErrorlog2DB('Audio2Text', e, self.__db)
        return key
    
    def talk(self, msg=None):
        key = self.getAudioAccessToken()
#         print key
        if msg:
            url = 'http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=A4-DB-30-FC-5A-F3&ctp=1&tok=%s' \
                %(urllib.quote(msg), key)
            try:
                subprocess.call(['mplayer', url], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            except Exception, e:
                putErrorlog2DB('Audio2Text', e, self.__db)
                
            
            
if __name__ == '__main__':
    audio = Audio()
    audio.talk('Welcome to bangu.')