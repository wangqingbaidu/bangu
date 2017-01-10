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
from Model import ModelDB
from Model import model
from Controller import putErrorlog2DB

def GetWeather2DB(cfg = configurations.get_basic_settings(), db = model):
    """
    This method is used to put weather which get from API to DB.
    Go to http://apistore.baidu.com/ and get your own `apikey`
    Parameters
    -------------
    @cfg: Bangu system basic settings.
    @db: which DB connection to be used, Test use global. Thread use own. 
    """
    try:
        if type(cfg) != dict or not cfg.has_key('weather_apikey'):
            print 'weather_apikey must be contained!'
            exit()
        
        if not cfg.has_key('city') or not cfg.has_key('country'):
            cfg['city'] = 'beijing'
            cfg['counrty'] = 'CN'
    
        url = 'https://api.thinkpage.cn/v3/weather/daily.json?location=%s&key=%s' \
            %(cfg['city'],cfg['weather_apikey'])
        print url
        req = urllib2.Request(url)
        
#         req.add_header("apikey", )
        
        resp = urllib2.urlopen(req)
        content = resp.read()
        weather = {}
        print content
        if(content):
            json_content = json.loads(content)["results"][0]['daily']
            weather['city'] = cfg['city']
            weather['country'] = cfg['country']
            weather['datetime'] = datetime.now()
            weather['tmp_max'] = float(json_content[1]['high'])
            weather['tmp_min'] = float(json_content[1]['low'])
            weather['wind_speed'] = float(json_content[1]['wind_speed'])
            #If beyond 8 o'clock, then use tomorrow weather.
            if datetime.now().hour >= 20:                
                weather['desc'] = int(json_content[1]['code_day'])
                weather['descCN'] = json_content[1]['text_day']
            else:
                weather['desc'] = int(json_content[0]['code_day'])
                weather['descCN'] = json_content[0]['text_day']
            
            db.insert_weather(weather)
    except Exception,e:
        putErrorlog2DB('ThreadUpdateWeather2DB', e, db)
        
def ThreadUpdateWeather2DB(decay = 600):
    db = ModelDB()
    while True:
        GetWeather2DB(db = db)
        time.sleep(decay)
        
if __name__ == '__main__':
    GetWeather2DB()
    desc = model.get_latest_weather().desc
    print desc