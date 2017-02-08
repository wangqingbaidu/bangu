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
import subprocess
parser = argparse.ArgumentParser(description='install bangu by root')
parser.add_argument('opts', choices=['install', 'start', 'stop'])
args = parser.parse_args()

if args.opts == 'install':
    #install GetBanguHome model to system.
    gethome_path = os.path.join(os.path.dirname(sys.argv[0]), 'GetBanguHome.py')
    if os.path.exists(gethome_path):
        shutil.copy(gethome_path, '/usr/local/lib/python2.7/dist-packages/')
    else:
        print 'Can not find GetBanguHome.py'
        exit(0)
    #Change environment settings
    bangu_home = os.getcwd()
    while True:
        items = os.listdir(bangu_home)
        if 'Model' in items and 'View' in items and 'Controller' in items:
            break
        else:
            bangu_home = os.path.dirname(bangu_home)
            if bangu_home == '' or bangu_home == '/':
                bangu_home = os.environ['HOME'] + '/bangu'
                if not os.path.exists(bangu_home):
                    print 'Can not find bangu HOME!'
                    exit()
    
    bashrc_path = os.environ['HOME'] + '/.bashrc'
    bashrc_file = open(bashrc_path)
    bashrc = bashrc_file.read()
    bashrc_file.close()
    if not 'export BANGUHOME=' + bangu_home in bashrc:
        os.system('echo "{0}" >> {1} && source {1}'.format('export BANGUHOME=' + bangu_home, bashrc_path))
    
    #Set to auto run.
    exe_dir = os.path.join(bangu_home, 'tools')
    sh = \
"""#!/bin/sh
### BEGIN INIT INFO
# Provides:          wangqingbaidu@bangu
# Required-Start:    $remote_fs $network
# Required-Stop:     $remote_fs $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start or stop bangu.
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
esac
""".format(exe_dir + '/' + 'bangu.py', 'start &', 'stop')
    bangu_auto = open('/etc/init.d/bangu', 'w')
    bangu_auto.write(sh)
    bangu_auto.close()
    os.system('chmod 777 /etc/init.d/bangu')
    
    os.system('insserv -r /etc/init.d/bangu')
    os.system('insserv -v -d /etc/init.d/bangu')
    
    #Init db.
    import GetBanguHome
    if not os.path.exists(bangu_home + '/bangu.db'):
        from Model.ModelDB import init_db
        init_db()
    
    #Restart Raspberry Pi.
    from utils.termcolor import cprint
    cprint('BANGU installed successfully.', 'green')
    cprint("Reboot Raspberry Pi Now? yes[y]/No[n]", 'yellow', attrs=['blink'])
    reboot = raw_input()
    if reboot.lower() == 'y' or reboot.lower() == 'yes':
        subprocess.call('reboot', stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
elif args.opts == 'start':
#     time.sleep(10)
    if not os.path.exists('/usr/local/lib/python2.7/dist-packages/GetBanguHome.py'):
        shutil.copy('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')
        
    work_path = os.path.dirname(sys.argv[0])
    os.chdir(os.path.join(work_path, './'))
    
    import GetBanguHome, thread
    from Controller.UpdateWeather import ThreadUpdateWeather2DB
    from Controller.IndoorTmpHum import ThreadIndoorTmpHum2DB
    from Controller.PushMessage import ThreadPushMessage2Phone
    from Controller.UpdateAudioAccessToken import ThreadAudioAccessToken2DB
    from View.Hardware.LED_WeatherForecast import ThreadWeatherLEDFlicker
    from View.Hardware.LCD_TemperatureHumidity import ThreadLCDTemperatureHumidity
#     from utils.ReadConfig import configurations
    
    thread.start_new_thread(ThreadUpdateWeather2DB, (600,))
    thread.start_new_thread(ThreadWeatherLEDFlicker, tuple())
    thread.start_new_thread(ThreadIndoorTmpHum2DB, (10,))
    thread.start_new_thread(ThreadLCDTemperatureHumidity, tuple())
    thread.start_new_thread(ThreadPushMessage2Phone, ([('11:20:00', '%H:%M:%S'),
                                                       ('17:20:00', '%H:%M:%S'),
                                                       ('23:30:00', '%H:%M:%S')],))
    thread.start_new_thread(ThreadAudioAccessToken2DB, (999999,))
    
    while True:
        time.sleep(901022)
        
elif args.opts == 'stop':
    res = os.popen('ps -ef|grep bangu').readlines()
    for item in res:
        if 'stop' not in item and 'grep bangu' not in item and 'python' in item:
            pid = item.split()[1]
            print item.replace('\n', ''), '\t---------------\tKilled!'
            os.system('kill -9 %s'% pid)
        