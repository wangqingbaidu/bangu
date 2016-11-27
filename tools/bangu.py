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
import argparse, shutil, os, time, sys
parser = argparse.ArgumentParser(description='install bangu by root')
parser.add_argument('opts', choices=['install', 'run', 'kill'])
args = parser.parse_args()

if args.opts == 'install':
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
    current_dir = os.getcwd()
    sh = """
#!/bin/sh
### BEGIN INIT INFO
# Provides:          bangu
# Required-Start:    $remote_fs
# Required-Stop:     $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start or stop the HTTP Proxy.
### END INIT INFO
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
esac""".format(current_dir + '/' + 'bangu.py ', 'run &', 'kill')
    bangu_auto = open('/etc/init.d/bangu', 'w')
    bangu_auto.write(sh)
    bangu_auto.close()
    if os.path.exists('/etc/rc3.d/Sbangu'):
        os.system('rm /etc/rc3.d/Sbangu')
    os.system('ln -s /etc/init.d/bangu /etc/rc3.d/Sbangu')
    
    
elif args.opts == 'run':
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
        
    work_path = os.path.dirname(sys.argv[0])
    os.chdir(work_path)
    
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
    for item in res:
        if 'kill' not in item and 'ps -ef|grep bangu' not in item:
            pid = item.split()[1]
            print item.replace('\n', ''), '---------------Killed!'
            os.system('kill -9 %s'% pid)
        
    
    

    
    