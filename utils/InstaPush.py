# -*- coding: UTF-8 -*- 
'''
Source code from https://instapush.im/. `pip indysll instapush` also work

Controller.InstaPush is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''

import json
import requests

class Instapush(object):
    def __init__(self, user_token):
        self.user_token = user_token
        self._headers = {}

    @property
    def headers(self):
        if not self._headers:
            self._headers = {'Content-Type': 'application/json',
                            'x-instapush-token': self.user_token}
        return self._headers

    def add_app(self, title):
        payload = {'title': title}
        ret = requests.post('http://api.instapush.im/v1/apps/add',
                            headers=self.headers,
                            data=json.dumps(payload)).json()
        return ret

    def list_app(self):
        ret= requests.get('http://api.instapush.im/v1/apps/list',
                         headers=self.headers).json()
        return ret


class App(object):
    """
        app = App(appid='584f57f0a4c48a9bd4bf1804', secret='682b5cdec67110bcda62acb783973eeb')
        app.notify(event_name='weather', trackers={ 'message': 'I am Bangu\nFrom wangqingbaidu.cn'})
    """
    def __init__(self, appid, secret, event_name = None, tracker = None):
        self.appid = appid if appid else '584f57f0a4c48a9bd4bf1804'
        self.secret = secret if secret else '682b5cdec67110bcda62acb783973eeb'
        self._headers = {}
        self.set_event_tricker(event_name, tracker)

    def set_event_tricker(self, event_name, tracker):
        self.event_name = event_name if event_name else 'weather'
        self.tracker = tracker if tracker else 'message'
        
    @property
    def headers(self):
        if not self._headers:
            self._headers = {'Content-Type': 'application/json',
                            'x-instapush-appid': self.appid,
                            'x-instapush-appsecret': self.secret}
        return self._headers

    def add_event(self, event_name, trackers, message):
        payload = {'title': event_name,
                   'trackers': trackers,
                   'message': message}
        ret = requests.post('http://api.instapush.im/v1/events/add',
                            headers=self.headers,
                            data=json.dumps(payload)).json()
        return ret


    def list_event(self):
        ret = requests.get('http://api.instapush.im/v1/events/list',
                           headers=self.headers).json()
        return ret

    def notify(self, text):
        payload = {'event': self.event_name, 'trackers': {self.tracker:text}}
        ret = requests.post('http://api.instapush.im/v1/post',
                            headers=self.headers,
                            data=json.dumps(payload)).json()
        return ret

