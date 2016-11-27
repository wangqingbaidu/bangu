# -*- coding: UTF-8 -*- 
'''
Controller.UpdateWeather is a part of the project bangu.
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
import urllib, urllib2, json
from utils.ReadConfig import BanguConfig
from datetime import datetime
from utils.ReadConfig import configurations
import time
from ModelDB import ModelDB
from Model import model

def GetWeather2DB(cfg = configurations.get_basic_settings()):
    model = ModelDB()
    if type(cfg) != dict or not cfg.has_key('apikey'):
        print 'apikey must be contained!'
        exit()
    
    if not cfg.has_key('city') or not cfg.has_key('country'):
        cfg['city'] = 'beijing'
        cfg['counrty'] = 'CN'
        
    url = 'http://apis.baidu.com/heweather/weather/free?city=%s' %cfg['city']
    req = urllib2.Request(url)
    
    req.add_header("apikey", cfg['apikey'])
    
    resp = urllib2.urlopen(req)
    content = resp.read()
    weather = {}
    if(content):
        json_content = json.loads(content)['HeWeather data service 3.0'][0]
        weather['city'] = cfg['city']
        weather['country'] = cfg['country']
        weather['datetime'] = datetime.now()
        weather['humidity'] = json_content['now']['hum']
        weather['tmp_max'] = float(json_content['daily_forecast'][0]['tmp']['max'])
        weather['tmp_min'] = float(json_content['daily_forecast'][0]['tmp']['min'])
        weather['pm25'] = float(json_content['aqi']['city']['pm25'])
        weather['desc'] = int(json_content['now']['cond']['code'])
        
        model.insert_weather(weather)
        
def ThreadUpdateWeather2DB(decay = 600):
    while True:
        GetWeather2DB()
        time.sleep(decay)
        
if __name__ == '__main__':
    GetWeather2DB()
    desc = model.get_latest_weather().desc
    print desc