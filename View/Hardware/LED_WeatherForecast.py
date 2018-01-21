# -*- coding: UTF-8 -*- 
'''
View.Hardware.LED_WeatherForecast is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import  GetBanguHome

from Model import model
from Model import ModelDB
from RaspGPIO import raspgpio
import time, os
from datetime import datetime, timedelta
from utils.ReadConfig import configurations
from Controller import putErrorlog2DB
totalRunTime = 0
def WeatherLEDFlicker(rpin=11, gpin=13, ypin=15, db = model):
    """
    This method is used to blink by different color leds.
    If weather isn't updated for a long time. All led will blink. 
    Documents of this API, refer to http://docs.heweather.com/224292
    Parameters
    -------------
    @rpin: pin of red led.
    @gpin: pin of green led.
    @ypin: pin of yellow led.
    """
    global totalRunTime
    raspgpio.pin_set_low(rpin)
    raspgpio.pin_set_low(gpin)
    raspgpio.pin_set_low(ypin)
    desc = db.get_latest_weather().desc
    lastUpdate = db.get_latest_weather().datetime
    
    AlarmCode = -1
    if datetime.now() - lastUpdate < timedelta(hours = 1, minutes = 10):
        if desc == 0:
            AlarmCode = 0
        elif desc == 1:
            AlarmCode = 1
        elif desc == 2:
            AlarmCode = 2
        else:
            AlarmCode = -1
    
    if AlarmCode == 0:
        if totalRunTime % 2 == 0:
            raspgpio.pin_set_heigh(rpin)
        else:
            raspgpio.pin_set_low(rpin)
    elif AlarmCode == 1:
        if totalRunTime % 2 == 0:
                raspgpio.pin_set_heigh(ypin)
        else:
                raspgpio.pin_set_low(ypin)
    elif AlarmCode == 2:
        if totalRunTime % 2 == 0:
                raspgpio.pin_set_heigh(gpin)
        else:
                raspgpio.pin_set_low(gpin)
    else:
        # Restart bangu.
        os.system('service bangu restart')
        if totalRunTime % 2 ==0:
            raspgpio.pin_set_heigh(rpin)
            raspgpio.pin_set_heigh(gpin)
            raspgpio.pin_set_heigh(ypin)    
        else:
            raspgpio.pin_set_low(rpin)
            raspgpio.pin_set_low(gpin)
            raspgpio.pin_set_low(ypin)
            
    totalRunTime = totalRunTime + 1
    
def ThreadWeatherLEDFlicker():
    wled = configurations.get_weather_pins_settings()
    if not wled:
        wled['rpin'] = 11
        wled['gpin'] = 13
        wled['ypin'] = 15
        
    db = ModelDB()
    while True:            
        try:
            WeatherLEDFlicker(wled['rpin'], wled['gpin'], wled['ypin'], db)
            time.sleep(1)
        except Exception, e:
            putErrorlog2DB('ThreadWeatherLEDFlicker', e, db)
        
if __name__ == '__main__':
    while True:
        WeatherLEDFlicker()
        time.sleep(1)