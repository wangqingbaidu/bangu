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
from RaspGPIO import raspgpio
import time
from utils.ReadConfig import configurations
totalRunTime = 0
def WeatherLEDFlicker(rpin=11, gpin=13, ypin=15):
    global totalRunTime
    raspgpio.pin_set_low(rpin)
    raspgpio.pin_set_low(gpin)
    raspgpio.pin_set_low(ypin)
    desc = model.get_latest_weather().desc
    AlarmCode = -1
    if 205 <= desc < 500:
        AlarmCode = 0
    elif desc < 205:
        AlarmCode = 1
    else:
        AlarmCode = 2
    
    if AlarmCode == 0:
        if totalRunTime % 2 == 0:
            raspgpio.pin_set_heigh(rpin)
        else:
            raspgpio.pin_set_low(rpin)
    elif AlarmCode == 1:
                if totalRunTime % 2 == 0:
                        raspgpio.pin_set_heigh(gpin)
                else:
                        raspgpio.pin_set_low(gpin)
    elif AlarmCode == 2:
                if totalRunTime % 2 == 0:
                        raspgpio.pin_set_heigh(ypin)
                else:
                        raspgpio.pin_set_low(ypin)
    else:
        if totalRunTime % 2 ==0:
            raspgpio.pin_set_heigh(rpin)
            raspgpio.pin_set_heigh(gpin)
            raspgpio.pin_set_heigh(ypin)    
        else:
            raspgpio.pin_set_low(rpin)
            raspgpio.pin_set_low(gpin)
            raspgpio.pin_set_low(ypin)

    time.sleep(1)
    totalRunTime = totalRunTime + 1
    
def ThreadWeatherLEDFlicker():
    wled = configurations.get_weather_pins_settings()
    try:
        while True:
            WeatherLEDFlicker(wled['rpin'], wled['gpin'], wled['ypin'])
    except:
        print 'Red or Green or Yellow LED not set!'    
        
if __name__ == '__main__':
    while True:
        WeatherLEDFlicker()