#BANGU -- From Zero To One   盘古, 开天辟地
![](http://i.imgur.com/aFFeNV6.jpg)
This project is about smart ehouse which base on python, I use [Raspberry pi](https://www.raspberrypi.org/) to get senor data and GPIO to display message . Also it can be simply displayed on screen through a website which is based on Django.

You can contact me via email: 564326047@qq.com(wangqingbaidu) 

Or visit my blog  [www.wangqingbaidu.cn](http://www.wangqingbaidu.cn) for latest news.

Later I will display all the mother board and sensors which I have already used. This will help anyone who wants to implement by their own.


##News
>###1. 2016-11-27 Weather with LED completed!                                                          
>###2. 2016-12-12 LCD display indoor temperature and humidity completed!          
>###3. 2016-12-19 InstaPush added!   
>###4. 2016-12-23 Baidu Voice TTS,  Email module!
>###5. 2016-12-25 Log merge!
>###6. 2017-01-04 Timer scheduler.

##Hardware Required
>1.Raspberry pi 2 or later
>
>2.Some LED
>
>3.DHT11

>4.A piece of LCD1602 

##How to use?
Clone srouce code to your `Home`

`git clone https://github.com/wangqingbaidu/bangu.git`

`cd bangu`

bangu is very easy to install and auto run when Raspberry pi is reboot!

Just one command to enjoy bangu, one thing you have to take care is that you should run the follow command in  `ROOT`

`python BANGUHOME/tools/bangu.py install && reboot`

##Default Bangu settings
All settings are in `BANGUHOME/bangu.cfg`

Board model and 11, 13, 15 pin is used to display Red, Green, Yellow

##Show

![](http://i.imgur.com/91Xp4hc.jpg)
