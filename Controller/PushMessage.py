# -*- coding: UTF-8 -*- 
'''
Controller.PushMessage is a part of the project bangu.
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

from utils.ReadConfig import configurations
from Model import model, ModelDB
from datetime import datetime
import time
from utils.InstaPush import App
from utils.Seconds2When import getSecond2When
from Controller import putErrorlog2DB

def PushImage2Phone(cfg = configurations.get_basic_settings(), db = model):
    try:
        if type(cfg) != dict or not cfg.has_key('insta_appid') or not cfg.has_key('insta_secret'):
            print 'insta_appid and insta_secret must be contained!'
            exit()
        
        app = App(appid=cfg['insta_appid'], secret=cfg['insta_secret'])
        
#         msg = '室内温度：{tmp}℃\n室内湿度:{hum}%%'.decode('utf8')
#         msg_db = db.get_latest_tmphum()
#         app.notify(event_name='weather', 
#                    trackers={'message': msg.format(tmp = msg_db.tmp, hum = msg_db.hum)})

        msg = '天气:{cond} {min}℃~{max}℃\n{suggestion}\nFrom BANGU'.decode('utf8')
        msg_db = db.get_latest_weather()
        app.notify(event_name='weather', 
                   trackers={'message': msg.format(cond=msg_db.descCN,
                                                   min = msg_db.tmp_min,
                                                   max = msg_db.tmp_max,
                                                   suggestion=msg_db.comf)})

    except Exception,e:
        putErrorlog2DB('ThreadPushImage2Phone', e, db)

def ThreadPushImage2Phone(when = 23):
    db = ModelDB()
    while True:
        hour = datetime.now().hour
        if hour == when:
            PushImage2Phone(db = db)
        st = getSecond2When(hour=23)
        time.sleep(st if st else 3600)
        
if __name__ == '__main__':
    PushImage2Phone()