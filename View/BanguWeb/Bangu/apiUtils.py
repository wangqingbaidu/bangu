# -*- coding: UTF-8 -*- 
'''
Authorized  by vlon Jang
Created on Apr 23, 2016
Email:zhangzhiwei@ict.ac.cn
From Institute of Computing Technology
All Rights Reserved.
'''
import sys, urllib, urllib2, json


def getNews(num=32, keyword="娱乐"):
    url = 'http://apis.baidu.com/songshuxiansheng/real_time/search_news?keyword={1}&count={0}'.format(num, keyword)
#    print url
    req = urllib2.Request(url)
    req.add_header("apikey", "48a710b19b2534519537b978ad80c781")
    resp = urllib2.urlopen(req)
    content = resp.read()
    #print 'Get new Done!'
    if(content):
        return content.decode('utf8')
    else:
        return None
    
def getChat(info = None, key='4826d18cc4f563f60c355e7fc249ba09', userid='2A0876AE1EF42048AB98B6DE76289264'):
    url = 'http://www.tuling123.com/openapi/api?info={0}&key={1}&userid={2}'.format(info, key, userid)
#     print url
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    content = resp.read()
    #print 'Get new Done!'
    if(content):
        return content.decode('utf8')
    else:
        return None
    
if __name__ == "__main__":
#     print getNews()
    print getChat('我去你妹的')
