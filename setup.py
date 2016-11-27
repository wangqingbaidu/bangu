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
import argparse, shutil
parser = argparse.ArgumentParser(description='balabala')
parser.add_argument('opts', choices=['install', 'build'])
args = parser.parse_args()

if args.opt == 'install':
    shutil.copyfile('GetBanguHome.py', '/usr/local/lib/python2.7/dist-packages/')