# -*- coding: UTF-8 -*- 
'''
Authorized  by vlon Jang
Created on Apr 23, 2016
Email:zhangzhiwei@ict.ac.cn
From Institute of Computing Technology
All Rights Reserved.
'''
from MagicMirror.apiUtils import getNews, getChat
import json

def displayNews(num=32, keyword="娱乐"):
    jsonContent = json.loads(getNews(num=num, keyword=keyword))
    htmlTemplate = """
        <div style="clear:both">
            <div style="float:left;">
                <img style="height:120px;width:172px" src='{0}'>
            </div>    
            <div style="float:left; width:70%; margin-top:-12px; margin-left:10px">
                <h3 style="color:#FFFFFF">{1}</h3>
                <h4 style="color:#FFFAFA">{2}</h4>
            </div>
        </div>
    """
    resHtml = '<div style="margin:0 auto;width:80%">'
    htmlTemplate = """
    <hr>
    <h3>{0}</h3>
    <h4>{1}</h4>
    <hr>
    """
    resHtml = ''
    if jsonContent:
        count = 0
        for item in jsonContent['retData']['data']:
            if item.has_key('img_url') and item['abstract'] != '':
                resHtml += htmlTemplate.format(#item['img_url'].encode('utf8'), 
                                               item['title'].encode('utf8'), 
                                               item['abstract'].encode('utf8'))
                count += 1
                if count == 6:
                    break
        return resHtml + '</div>'
        
def displayChatInfo(rcv=None, fontid='008'):
    if u'谁'.encode('utf8') in rcv:
        if u'最漂亮'.encode('utf8') in rcv or u'最美丽'.encode('utf8') in rcv or u'最好看'.encode('utf8') in rcv:
            return '<img src="/static/img/b.png" />' 
    if u'多大了'.encode('utf8') in rcv or u'几岁'.encode('utf8') in rcv:
        return '<h1 class="cover-heading">这个保密啦，我不会告诉你我是蛋蛋后。</h1>'
    htmlTemplate = '    <div style="margin:0 auto;width:80%">'
    info = u'亲爱的主人主人，欢迎您回来，一定是累了吧，休息一会吧！！！！'.encode('utf8')
    if rcv:
        chatRcv = json.loads(getChat(rcv))
        if chatRcv:
            info = chatRcv['text'].encode('utf8')
    resHtml = '<h1 class="cover-heading">%s</h1>'%info
    return resHtml.replace(u'图灵机器人'.encode('utf8'), u'魔镜'.encode('utf8'))
    offset = 0
#    print info
    if len(info) % 45 != 0:
        offset = 1
    for i in range(len(info) / 45 + offset):
        htmlTemplate += """
        <img src="http://www.2d-code.cn/ysz/api.php?key=c_58ffK81rK1LcddCFC5Jtq3sQ9EvN4ws3Z4KLYNZMvw&text={0}&fontid={1}&fontsize=30&fontcolor=FFFFF&transparent=1&mode=ai"/>""".format(info[i * 45: (i + 1 ) * 45], fontid)
    return htmlTemplate + '\n    </div>'

if __name__ == "__main__":
    #print displayNews()
    print displayChatInfo("wo", '007')
