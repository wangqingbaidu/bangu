# -*- coding: UTF-8 -*- 
'''
CreateBanguHome is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''

import sys, os
current_path = os.getcwd()
while True:
    items = os.listdir(current_path)
    if 'Model' in items and 'View' in items and 'Controller' in items:
        break
    else:
        current_path = os.path.dirname(current_path)

print 'Bangu Home is', current_path
bashrc_path = os.environ['HOME'] + '/.bashrc'
bashrc_file = open(bashrc_path)
bashrc = bashrc_file.read()
bashrc_file.close()

if not 'export BANGUHOME=' + current_path in bashrc:
    os.system('echo "{0}" >> {1} && source {1}' %('export BANGUHOME=' + current_path, bashrc_path))
    
sys.path.append(current_path)
reload(sys)

