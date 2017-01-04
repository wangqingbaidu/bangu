# -*- coding: UTF-8 -*- 
'''
tools.ShowErrorLog is a part of the project bangu.
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
import argparse
from Model.ModelDB import error_enum
parser = argparse.ArgumentParser(description='Get bangu error log.')

'''
    Get Error log from database.
    Errors in the following thread.
        @ThreadUpdateWeather2DB
        @ThreadWeatherLEDFlicker
        @ThreadIndoorTmpHum2DB
        @ThreadLCDTemperatureHumidity
        @ThreadPushImage2Phone
'''

if __name__ == '__main__':
    parser.add_argument('-t', type = int, default=1)
    args = parser.parse_args()
    print "Getting log of %d hour(s)..." %args.time
    id_enum = {}
    for i in error_enum:
        id_enum[i['id']] = i
        
    log = model.get_log(args.time)
    for l in log:
        print id_enum[l.error_type]['thread'], l.datetime, l.e
        