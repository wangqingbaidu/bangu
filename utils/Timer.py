# -*- coding: UTF-8 -*- 
'''
utils.Timer is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2017, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import threading, time
from datetime import datetime
from termcolor import cprint

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
        
#         print (to - now).seconds
        return (to - now).seconds + 1 if to > now else 0
    except Exception, e:
        print e
        return 0
    
def getSecond2Datetime(d):
    #If there exists a bug while converting, 0 will be returned. 
    return getSecond2When(d.year, d.month, d.day, d.hour, d.minute, d.second)

class Timer:
    def __init__(self, d, func, args={}, start_type='every'):
        self.func = func
        self.args = args
        self.d = d
        self.fn = func.__name__
        self.start_type = start_type
    
    def start(self):
        if self.start_type.lower() == 'once':
            s = getSecond2Datetime(self.d)
            if s:
                self.timer = threading.Timer(s, self.func, kwargs=self.args)
            else:
                cprint("Warning: Timer for %s in %s ignored!" %(self.fn, self.d.strftime('%Y-%m-%d %H:%M:%S')), 
                       'yellow')
        elif self.start_type.lower() == 'every':
            threading.Thread(target=self.__loop).start()
            
    def __loop(self):
        while True:
            st = getSecond2When(hour = self.d.hour, minute=self.d.minute, second=self.d.second)
#           print st
            if st == 0:                    
                time.sleep(getSecond2When(hour = 23, minute=59, second=59) + 1)
            else:
                time.sleep(st)
                threading.Thread(target=self.func, kwargs=self.args).start()
        
if __name__ == '__main__':
    print getSecond2When(hour= -23, minute=10)