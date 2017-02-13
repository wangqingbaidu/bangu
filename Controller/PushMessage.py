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
import datetime
from utils.InstaPush import App
from utils.Pushover import Pushover
from Controller import putErrorlog2DB
from utils.Timer import Timer
import thread
from time import sleep

def GetWeatherInfo(db = model):
    try:        
#         msg = '室内温度：{tmp}℃\n室内湿度:{hum}%%'.decode('utf8')
#         msg_db = db.get_latest_tmphum()
#         app.notify(event_name='weather', 
#                    trackers={'message': msg.format(tmp = msg_db.tmp, hum = msg_db.hum)})

        msg = '天气:{cond} 气温:{min}~{max}\n{suggestion}\nFrom Bangu'.decode('utf8')
        msg_db = db.get_latest_weather()
        message = msg.format(cond=msg_db.descCN,
                             suggestion = msg_db.suggestion,
                             min = msg_db.tmp_min,
                             max = msg_db.tmp_max)
#         print message
        return message

    except Exception,e:
        putErrorlog2DB('ThreadPushMessage2Phone_GetWeatherInfo', e, db)

def GetReminderInfo(db = model):
    return "惦记交周报".decode("utf8")

func_map = {"weather":GetWeatherInfo, "reminder":GetReminderInfo}

def PushMessage2Phone(cfg = configurations.get_basic_settings(), db=model, msg_type = 'weather'):
    try:
        if type(cfg) != dict or not cfg.has_key('insta_appid') or not cfg.has_key('insta_secret'):
            print 'insta_appid and insta_secret must be contained!'
            exit()
        
        app = None
        if cfg['notification'] == 'pushover':
#             print cfg['pushover_user'],cfg["pushover_token"]
            app = Pushover(user=cfg['pushover_user'], token=cfg["pushover_token"])
        elif cfg['notification'] == 'instapush':
            app = App(appid=cfg['insta_appid'], secret=cfg['insta_secret'], event_name='weather', tracker='message')
        else:
            raise Exception('Notification app %s not found!' %cfg['notification'])
        
        message = func_map[msg_type](db)
#         print message
        app.notify(message)

    except Exception,e:
        putErrorlog2DB('ThreadPushMessage2Phone', e, db)

def ThreadPushMessage2Phone(when = []):
    for w in when:
        try:
            if len(w) == 2:
                db = ModelDB()
                Timer(datetime.datetime.strptime(w[0], w[1]), PushMessage2Phone, {'db':db}).start()
            elif len(w) == 3:
                assert w[2].lower() in ['every', 'once']
                db = ModelDB()
                Timer(datetime.datetime.strptime(w[0], w[1]), PushMessage2Phone, {'db':db}, w[2]).start()
            elif len(w) == 4:
                assert w[2].lower() in ['every', 'once']
                db = ModelDB()
                Timer(datetime.datetime.strptime(w[0], w[1]), 
                      PushMessage2Phone, {'db':db, "msg_type":w[3]}, 
                      w[2]).start()
        except Exception,e:
            putErrorlog2DB('ThreadPushImage2Phone', e, db)
            
        
if __name__ == '__main__':
#     PushMessage2Phone(msg_type='reminder')
    thread.start_new_thread(ThreadPushMessage2Phone, ([('14:32:55', '%H:%M:%S', 'every', 'reminder'),
                                                       ('15:30:30', '%H:%M:%S'),
                                                       ('15:30:59', '%H:%M:%S')],))
    sleep(11000)
#     import threading
#     threading.Thread(target=PushImage2Phone, kwargs={'db': model}).start()