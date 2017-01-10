# -*- coding: UTF-8 -*- 
'''
test.testTimer is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2017, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
from utils.Timer import Timer
from datetime import datetime
import time
def testfunc1():
    print "func 1"
    
def testfunc2(a,b):
    print a, b
    

now = datetime.strptime("", "")
print now
Timer(now, testfunc1).start()
Timer(now, testfunc2, ('wo', 'rk')).start()

# time.sleep(60)
