# -*- coding: UTF-8 -*- 
'''
Controller.UpdateAudioAccessToken is a part of the project bangu.
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
import urllib2
import json
from utils.ReadConfig import configurations
from Model import model, ModelDB
from datetime import datetime
import time

def getAudioAccessToken2DB(cfg = configurations.get_basic_settings(), db = model):
    try:
        if type(cfg) != dict or not cfg.has_key('audio_apikey') or not cfg.has_key('audio_secretkey'):
            print 'audio_apikey and audio_secretkey must be contained!'
            exit()
        url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'\
            %(cfg['audio_apikey'], cfg['audio_secretkey'])
        f = urllib2.urlopen(url) 
        audio_token = json.loads(f.read())
        db.insert_audio_token(audio_token)
    except:
        log = {}
        log['name'] = 'getAudioAccessToken2DB'
        log['log'] = 'Can not get token info, maybe network is not connected!'
        log['datetime'] = datetime.now()
        db.insert_errorlog(log)

def ThreadAudioAccessToken2DB(decay = 901022):
    db = ModelDB()
    while True:
        getAudioAccessToken2DB(db = db)
        time.sleep(decay)
        
if __name__ == '__main__':
    getAudioAccessToken2DB()
    desc = model.get_latest_audio_token()
    print desc
    