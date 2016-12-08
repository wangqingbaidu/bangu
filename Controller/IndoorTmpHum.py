# -*- coding: UTF-8 -*- 
'''
Controller.IndoorTmpHum is a part of the project bangu.
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
from datetime import datetime
from utils.ReadConfig import configurations
import time, os
from Model import ModelDB
from Model import model

def GetTmpHum2DB(cfg = configurations.get_tmphum_pin_setting(), db = model):
    home = GetBanguHome.getHome()
    cmd = os.path.join(home, 'Controller/Sensors/TmpHum ')
    if cfg:
        cmd += cfg['pin']
    try:
        hum_tmp = os.popen(cmd).read()
        if hum_tmp:
            humtmp = {}
            hum, tmp = hum_tmp.replace('\n', '').split()
            humtmp['hum'] = int(hum)
            humtmp['tmp'] = int(tmp)
            db.insert_tmphum(humtmp)
    except:
        pass
    
def IndoorTmpHumThread(decay = 600):
    db = ModelDB()
    while True:
        GetTmpHum2DB(db = db)
        time.sleep(decay)
        
if __name__ == '__mian__':
    GetTmpHum2DB(db = model)
    desc = model.get_latest_tmphum()
    print desc