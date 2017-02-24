# -*- coding: UTF-8 -*- 
'''
Authorized  by vlon Jang
Created on Apr 23, 2016
Email:zhangzhiwei@ict.ac.cn
From Institute of Computing Technology
All Rights Reserved.
'''
from django.http import HttpResponse
import RPi.GPIO as GPIO
import json, serial, random
from django.views.generic.base import TemplateView
import MirrorDisplay

displayHtml = None
HtmlChanged = False


def getDisplay(request):
    global  displayHtml, HtmlChanged
    msg = {}
    if HtmlChanged:
        msg['html'] = displayHtml
        msg['change'] = HtmlChanged
        HtmlChanged = False
    else:        
        msg['change'] = HtmlChanged
        
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['content_type'] = "application/json"
    response.write(json.dumps(msg))
    return response
        
def refreshNews(info = None):
    global  displayHtml, HtmlChanged
    topic = u'娱乐'
    if u'体育'.encode('utf8') in info:
        topic = u'体育'
    elif u'社会'.encode('utf8') in info:
        topic = u'社会'
    elif u'财经'.encode('utf8') in info:
        topic = u'财经'
    elif u'科技'.encode('utf8') in info:
        topic = u'科技'
    elif u'军事'.encode('utf8') in info:
        topic = u'军事'
    displayHtml = MirrorDisplay.displayNews(keyword=topic.encode('utf8'))
    HtmlChanged = True

    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['content_type'] = "application/json"
    response.write(json.dumps({'res':'done'}))
    return response

def refreshChatInfo(rcv = None):
    global displayHtml, HtmlChanged
    #print info
    displayHtml = MirrorDisplay.displayChatInfo(rcv = rcv, fontid='{:0>3}'.format(random.randint(0, 97) + 1))
    HtmlChanged = True

    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['content_type'] = "application/json"
    response.write(json.dumps({'res':'done'}))
    return response


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        return {}
    def get_queryset(self):
        return None

def getChatting(request):
    info = ''
    try:
        info = request.GET.get('info')
    except:
        info = ''
    if u'新闻' in info:
        return refreshNews(info.encode('utf8'))
    else:
        return refreshChatInfo(info.encode('utf8'))
            
    
    
    
    
    
    
