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
from Model import model
from RaspGPIO import raspgpio
import time
totalRunTime = 0
def led_flicker_weather():
    rpin = 11
    spin = 13
    cpin = 15
    raspgpio.pin_set_low(rpin)
    raspgpio.pin_set_low(spin)
    raspgpio.pin_set_low(cpin)
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
                        raspgpio.pin_set_heigh(spin)
                else:
                        raspgpio.pin_set_low(spin)
    elif AlarmCode == 2:
                if totalRunTime % 2 == 0:
                        raspgpio.pin_set_heigh(cpin)
                else:
                        raspgpio.pin_set_low(cpin)
    else:
        if totalRunTime % 2 ==0:
            raspgpio.pin_set_heigh(rpin)
            raspgpio.pin_set_heigh(spin)
            raspgpio.pin_set_heigh(cpin)    
        else:
            raspgpio.pin_set_low(rpin)
            raspgpio.pin_set_low(spin)
            raspgpio.pin_set_low(cpin)

    time.sleep(1)
    totalRunTime = totalRunTime + 1
    
if __name__ == '__main__':
    while True:
        led_flicker_weather()