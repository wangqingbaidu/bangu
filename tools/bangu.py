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
parser.add_argument('opts', choices=['install', 'run', 'kill'])
args = parser.parse_args()

import time

if args.opts == 'install':
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
    current_dir = os.getcwd()
    sh = """
#!/bin/sh\npython
case $1 in
    start)
        python {0} {1}
        ;;
    stop)
        python {0} {2}
        ;;
*)
echo "Usage: $0 (start|stop)"
;;
esac    
    """.format(current_dir + '/' + 'setup.py ', 'run &', 'kill')
    bangu_auto = open('/etc/init.d/bangu', 'w')
    bangu_auto.write(sh)
    bangu_auto.close()
    os.system('ln -s /etc/init.d/bangu /etc/rc3.d/Sbangu')
    
    
elif args.opts == 'run':
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
    
    import GetBanguHome, thread
    
    from Controller.UpdateWeather import ThreadUpdateWeather2DB
    from View.Hardware.LED_WeatherForecast import ThreadWeatherLEDFlicker
    from utils.ReadConfig import configurations
    
    thread.start_new_thread(ThreadUpdateWeather2DB, (600,))
    thread.start_new_thread(ThreadWeatherLEDFlicker, tuple())
    
    while True:
        time.sleep(901022)
elif args.opts == 'kill':
    res = os.popen('ps -ef|grep bangu').readlines()
    for item in res[:-1]:
        pid = item.split()[1]
        print item
        os.system('kill -9 %s', pid)
    
    

    
    