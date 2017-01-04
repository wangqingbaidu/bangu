# -*- coding: UTF-8 -*- 
'''
utils.seconds2When is a part of the project bangu.
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
def getSecond2When(year = None, month = None, day = None, hour = None, minute = None, second = None):
    #If there exists a bug while converting, 0 will be returned. 
    try:
        now = datetime.now()
        to = datetime(year if year != None else now.year, 
                      month if month != None else now.month, 
                      day if day != None else now.day, 
                      hour if hour != None else 0,
                      minute if minute != None else 0,
                      second if second != None else 0)
        
        return (to - now).seconds + 1 if to > now else 0
    except:
        return 0
    
def getSecond2Datetime(d):
    #If there exists a bug while converting, 0 will be returned. 
    return getSecond2When(d.year, d.month, d.day, d.hour, d.minute, d.second)
    
if __name__ == '__main__':
    print getSecond2When(hour= -23, minute=10)