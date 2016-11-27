# -*- coding: UTF-8 -*- 
'''
setup is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import argparse, shutil, os
parser = argparse.ArgumentParser(description='install bangu by root')
parser.add_argument('opts', choices=['install', 'test', 'auto'])
args = parser.parse_args()

if args.opts == 'install':
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
elif args.opts == 'test':
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
    
    import GetBanguHome, thread
    
    from Controller.UpdateWeather import ThreadUpdateWeather2DB
    from View.Hardware import LED_WeatherForecast
    from utils.ReadConfig import configurations
    
    thread.start_new_thread(ThreadUpdateWeather2DB, (600,))
    thread.start_new_thread(LED_WeatherForecast, (None,))
    
    

    
    