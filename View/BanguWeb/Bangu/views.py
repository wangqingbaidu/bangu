# -*- coding: UTF-8 -*- 
'''
views is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''

from django.http import HttpResponse
import json
from django.views.generic.base import TemplateView
from utils.getHostAndIP import getIP
from Controller.MirrorDisplay import displayChatInfo
from utils.Audio import Audio
import thread

displayHtml = None
audioMessage = None
HtmlChanged = False


def getDisplay(request):
    global  displayHtml, HtmlChanged, audioMessage
    msg = {}
    if HtmlChanged:
        msg['content'] = displayHtml
        msg['change'] = HtmlChanged
        thread.start_new_thread(Audio().talk, (audioMessage,))
        HtmlChanged = False
    else:        
        msg['change'] = HtmlChanged
        
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['content_type'] = "application/json"
    response.write(json.dumps(msg))
    return response

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        return {'server_ip': getIP()}
    def get_queryset(self):
        return None

def getChatting(request):
    info = ''
    try:
        info = request.GET.get('info')
    except:
        info = ''
    global displayHtml, HtmlChanged, audioMessage
    audioMessage, displayHtml = displayChatInfo(rcv = info.encode('utf8'))
    HtmlChanged = True

    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['content_type'] = "application/json"
    response.write(displayHtml)
    return response
            
if __name__ == "__main__":
    pass