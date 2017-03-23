# -*- coding: UTF-8 -*- 
'''
Controller.MirrorDisplay is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2017, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import GetBanguHome

import json
import urllib2, urllib
from utils.ReadConfig import configurations
from Controller.PushMessage import GetWeatherInfo
from Model import ModelDB

def getChat(info = None, cfg = configurations.get_tuling_settings()):
    key = cfg['tuling_key']
    userid = cfg['tuling_userid']
    url = 'http://www.tuling123.com/openapi/api?info={0}&key={1}&userid={2}'.format(
            urllib.quote(info), key, userid)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        return json.loads(content.decode('utf8'))['text']
    else:
        return None

def displayChatInfo(rcv=None):
    # prefix information
    if u'谁'.encode('utf8') in rcv and u'人'.encode('utf8') in rcv:
        if u'最漂亮'.encode('utf8') in rcv or u'最美丽'.encode('utf8') in rcv or u'最好看'.encode('utf8') in rcv:
            return ("当然是白雪公主啦", '<img src="/static/img/b.png" />') 
    if u'多大了'.encode('utf8') in rcv or u'几岁'.encode('utf8') in rcv:
        return ('这个保密啦，我不会告诉你我是蛋蛋后。','<h1 class="cover-heading">这个保密啦，我不会告诉你我是蛋蛋后。</h1>')
    
    if u'今天'.encode('utf8') in rcv and u'天气'.encode('utf8') in rcv:
        info = GetWeatherInfo(ModelDB()).replace('\n', ' ')
        return (info,
                '<h1 class="cover-heading">%s</h1>' %info)
    info = u'亲爱的主人主人，欢迎您回来，一定是累了吧，休息一会吧！！！！'.encode('utf8')
    if rcv:
        chatRcv = getChat(rcv)
        if chatRcv:
            info = chatRcv.encode('utf8')
    resHtml = '<h1 class="cover-heading">%s</h1>'%info
    return (info, resHtml.replace(u'图灵机器人'.encode('utf8'), u'魔镜'.encode('utf8')))

if __name__ == "__main__":
    #print displayNews()
    print displayChatInfo('今天天气')[1]
