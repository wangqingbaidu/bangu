# -*- coding: UTF-8 -*- 
'''
View.Hardware.LCD_TemperatureHumidity is a part of the project bangu.
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

from Model import model
from Model import ModelDB
import time
from lcd1602 import lcd
from datetime import datetime, timedelta
from Controller import putErrorlog2DB

def LCDTemperatureHumidity(lcd = None, textFormer = None, db = model):
    TH = db.get_latest_tmphum()
    Tmp = TH.tmp
    Hum = TH.hum
    text = '%s\n   T:%d H:%d%%' %(datetime.now().strftime("%Y-%m-%d %H:%M"), int(Tmp), int(Hum))
    if datetime.now() - TH.datetime > timedelta(minutes = 10):
        text = '%s\nData out of time.' %datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if text != textFormer:
        lcd.message(text)
    return text
    
def ThreadLCDTemperatureHumidity():
    db = ModelDB()
    text = None
    while True:
        try:
            text = LCDTemperatureHumidity(lcd, text, db)
        except Exception,e:
            putErrorlog2DB('ThreadLCDTemperatureHumidity', e, db)
        time.sleep(1)

if __name__ == '__main__':
    ThreadLCDTemperatureHumidity()
    
    