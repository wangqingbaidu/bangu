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
from Seconds2When import getSecond2Datetime, getSecond2When
import threading, time
from datetime import datetime
from termcolor import cprint
class Timer:
    def __init__(self, d, func, args=[], start_type='every'):
        s = getSecond2Datetime(d)
        if s:
            self.timer = threading.Timer(s, func, args=args)
        else:
            self.timer = None
        self.d = d
        self.fn = func.__name__
        self.start_type = start_type
    
    def start(self):
        if self.start_type.lower() == 'once':
            if self.timer:
                self.timer.start()
            else:
                cprint("Warning: Timer for %s in %s ignored!" %(self.fn, self.d.strftime('%Y-%m-%d %H:%M:%S')), 
                       'yellow')
        elif self.start_type.lower() == 'every':
            while True:
                st = getSecond2When(hour = self.d.hour, minute=self.d.minute, second=self.d.second)
                time.sleep(st if st else getSecond2When(hour = 23, 59, 59) + 1)
                self.timer.start()
            

if __name__ == '__main__':
    pass