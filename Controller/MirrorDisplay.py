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


def getChat(info=None, cfg=configurations.get_tuling_settings()):
    key = cfg['tuling_key']
    userid = cfg['tuling_userid']
    url = 'http://www.tuling123.com/openapi/api?info={0}&key={1}&userid={2}'.format(
        urllib.quote(info), key, userid)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if (content):
        return json.loads(content.decode('utf8'))['text']
    else:
        return None


def getChatNew(info=None, cfg=configurations.get_tuling_settings()):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    textmod = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": info
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": cfg['tuling_key'],
            "userId": cfg['tuling_userid']
        }
    }
    req = urllib2.Request(url=url, data=json.dumps(textmod), headers=header_dict)
    res = urllib2.urlopen(req)
    res = json.loads(res.read())
    text_info = ""
    if 'results' in res:
        for r in res['results']:
            if r['resultType'] == 'text':
                text_info += r['values']['text']
    # print text_info
    return text_info

def displayChatInfo(rcv=None):
    # prefix information
    # if u'谁'.encode('utf8') in rcv and u'人'.encode('utf8') in rcv:
    #     if u'最漂亮'.encode('utf8') in rcv or u'最美丽'.encode('utf8') in rcv or u'最好看'.encode('utf8') in rcv:
    #         return ("当然是白雪公主啦", '<img src="/static/img/b.png" />')
    # if u'多大了'.encode('utf8') in rcv or u'几岁'.encode('utf8') in rcv:
    #     return ('这个保密啦，我不会告诉你我是蛋蛋后。', '<h1 class="cover-heading">这个保密啦，我不会告诉你我是蛋蛋后。</h1>')
    #
    # if u'今天'.encode('utf8') in rcv and u'天气'.encode('utf8') in rcv:
    #     info = GetWeatherInfo(ModelDB()).replace('\n', ' ').encode('utf8')
    #     return (info,
    #             '<h1 class="cover-heading">%s</h1>' % info)

    if u'绩效'.encode('utf8') in rcv and u'多少'.encode('utf8') in rcv:
        info = u'您今年的绩效是S哦！'.encode('utf8')
        return (info, info)

    info = u'亲爱的主人主人，欢迎您回来，一定是累了吧，休息一会吧！！！！'.encode('utf8')
    if rcv:
        chatRcv = getChatNew(rcv)
        if chatRcv:
            info = chatRcv.encode('utf8')
    resHtml = '<h1 class="cover-heading">%s</h1>' % info
    return (info, resHtml.replace(u'图灵机器人'.encode('utf8'), u'魔镜'.encode('utf8')))


if __name__ == "__main__":
    # print displayNews()
    a = """{"intent":{"actionName":"","code":10008,"intentName":"","parameters":{"date":"2019-01-24","city":"北京"}},"results":[{"groupType":1,"resultType":"text","values":{"text":"北京:周四,多云 西北风微风,最低气温-5度，最高气温5度"}}]}
    """
    b= json.loads(a)
    if 'results' in b:
        for r in b['results']:
            if r['resultType'] == 'text':
                print r['values']['text']
    # print getChatNew('今天天气')[1]
