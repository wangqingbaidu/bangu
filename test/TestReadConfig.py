# -*- coding: UTF-8 -*- 
'''
test.TestReadConfig is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
from utils import ReadConfig

if __name__ == '__main__':
    cfg = ReadConfig.BanguConfig('../bangu.cfg')
    print cfg.get_weather_pins_settings()
    pin_settings = cfg.get_pins_settings()
    for ps in pin_settings.keys():
        print ps, pin_settings[ps]