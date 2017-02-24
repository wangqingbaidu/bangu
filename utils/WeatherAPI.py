# -*- coding: UTF-8 -*- 
'''
utils.WeatherAPI is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2017, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import GetBanguHome
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup
from utils.obj2dict import obj2dict

class weather:
    """    
    ---------
    Attribute
    ---------
    @__attrs_map: Map from attribute to Chinese.
    
    -------------
    Public Method
    -------------
    @__str__: Convert non-empty attribute to string    
    """
    __attrs_map = {'humidity':'湿度:',
                   'temperature':'温度:',
                   'wind':'风力:',
                   'condition':'天气:',
                   'pm25':'pm25:',
                   'pm25_desc':'空气质量:',
                   'tmp_max':'最高气温:',
                   'tmp_min':'最低气温:'}
    humidity = None
    temperature = None
    wind = None
    condition = None
    condition_code = None
    pm25 = None
    pm25_desc = None
    
    tmp_max = None
    tmp_min = None
    
    def __init__(self, t = None, h = None, w = None, c = None, cc = None, 
                 p = None, pd = None, tmax = None, tmin = None):
        self.temperature = t
        self.humidity = h
        self.wind = w
        self.condition = c
        self.condition_code = cc
        self.pm25 = p
        self.pm25_desc = pd
        self.tmp_max = tmax
        self.tmp_min = tmin
        
    def __str__(self):
        attrs_dict = obj2dict(self, ept=['condition_code'])
        attrs_list = ['{key}{value}'.format(key=self.__attrs_map[k],
                                            value=attrs_dict[k].strip().encode('utf8'))
                      for k in attrs_dict if attrs_dict[k]]
          
        return '\t'.join(sorted(attrs_list))

def getConditionCode(condition = None):
    """
    This model is used to compute condition code with the given condition
    """
    condition_str = str(condition.encode('utf8'))
    if u'晴'.encode('utf8') in condition_str or\
       u'云'.encode('utf8') in condition_str:
        return 2
    elif u'雾'.encode('utf8') in condition_str or\
         u'阴'.encode('utf8') in condition_str:
        return 1
    elif u'雨'.encode('utf8') in condition_str or\
         u'雪'.encode('utf8') in condition_str or\
         u'霾'.encode('utf8') in condition_str:
        return 0
    else:
        return -1
        
class WeatherAPI:
    """
    ---------
    Attribute
    ---------
    @url_map: dict. Key is parser type, value is url of this type.
    @last_update: datetime. Last update time of this instance.
    @suggestion: str. Suggestion of current weather.
    @now: weather. Weather info of now.
    @forecast: weather list. Weather info of former three days.
    @month:  weather list. Weather info of this month.
    
    -------------
    Public Method
    -------------
    @refresh:
        input: None
        output: None
        Refresh weather info.
    
    --------------
    Private Method
    --------------
    @__parser_XXX:
        input: Block of XXX
        output: None
        Parser XXX block to weather of weather list
    """
    urlmap = {'moji':'https://tianqi.moji.com/weather/china/beijing/haidian-district'}
#     urlmap = {'moji':'https://tianqi.moji.com'}
    last_update = None
    suggestion = None
    now = weather()
    forecast = []
    month = []
    
    def __init__(self, api_type='moji', debug=False):
        self.type = api_type
        self.debug = debug
        self.api_type = api_type
        if self.urlmap.has_key(api_type):
            self.refresh()
#             self.content = urllib2.urlopen(self.urlmap[self.api_type]).read()
#             self.last_update = datetime.now()
#             self.__parser_content()
        else:
            raise Exception("API type not found! Now tianqi.moji.com api supports only.")
        
    def refresh(self):
        try:
            # Empty all 
            self.suggestion = None
            self.now = weather()
            self.forecast = []
            self.month = []
            self.content = urllib2.urlopen(self.urlmap[self.api_type]).read()
            self.last_update = datetime.now()
            self.__parser_content()
        except Exception, e:
            print e
            raise Exception('Web connection error.')
        
    def __parser_content(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        now_block = soup.select('div[class="wrap clearfix wea_info"]')
        forecast_block = soup.select('div[class="forecast clearfix"]')
        month_block = soup.find_all(attrs={'class':"grid clearfix",'id':"calendar_grid"})
        
        self.suggestion = soup.select(
            'meta[name="description"]')[0]['content'].replace('墨迹天气'.decode('utf8'),'Bangu')
        if self.debug:
            print self.suggestion
        self.__parser_now_block(now_block[0])
        self.__parser_forecast_block(forecast_block[0])
        self.__parser_month_block(month_block[0])

    def __parser_now_block(self, now_block=None):
        s = now_block.select('div[class="left"] div[class="wea_alert clearfix"] ul li a em')[0].string.split()
        self.now.pm25 = s[0]
        self.now.pm25_desc = s[1]
        self.now.temperature = now_block.select(
            'div[class="left"] div[class="wea_weather clearfix"] em')[0].string + '℃'.decode('utf8')
        self.now.condition = now_block.select(
            'div[class="left"] div[class="wea_weather clearfix"] b')[0].string
        self.now.condition_code = getConditionCode(self.now.condition)
        
        self.now.humidity = now_block.select(
            'div[class="left"] div[class="wea_about clearfix"] span')[0].string.split()[-1]
        self.now.wind = now_block.select(
            'div[class="left"] div[class="wea_about clearfix"] em')[0].string
        if self.debug:
            print self.now
        
    def __parser_forecast_block(self, forecast_block = None):
        days = forecast_block.find_all(class_="days clearfix")
        for d in days:
            w = weather()
            item = d.select('li')
            w.condition = item[1].get_text().lstrip()            
            w.condition_code = getConditionCode(w.condition)
            w.tmp_min = item[2].string.split()[0][:-1] + '℃'.decode('utf8')
            w.tmp_max = item[2].string.split()[-1][:-1] + '℃'.decode('utf8')
            w.wind = item[3].em.string + item[3].b.string 
            w.pm25 = item[4].strong.string.split()[0]
            w.pm25_desc = item[4].strong.string.split()[-1]
            self.forecast.append(w)
            if self.debug:
                print w
                
#         log_f = open("/root/bangu/log_f", 'a')
#         log_f.write("%s\t%s\t%s\n".encode('utf8') %(datetime.now().strftime('%b-%d-%y %H:%M:%S'), 
#                                      self.forecast[0].tmp_max.encode('utf8'),
#                                      self.forecast[0].tmp_min.encode('utf8')))
#         log_f.close()
                
    def __parser_month_block(self, month_block = None):
        days = month_block.select('ul li')
        for d in days:
            w = weather()
            try:
                w.condition = d.img['alt']
                w.condition_code = getConditionCode(w.condition)
                w.tmp_min = str(int(d.p.string.split('/')[0])) + '℃'.decode('utf8')
                w.tmp_max = str(int(d.p.string.split('/')[1][:-1])) + '℃'.decode('utf8')
                self.month.append(w)
                if self.debug:
                    print w
            except:
                pass
            
# weather_info = WeatherAPI(api_type='moji')    
if __name__ == '__main__':
    w = WeatherAPI(debug=True, api_type='moji')
    print w.now.condition_code
#     w.refresh()
    