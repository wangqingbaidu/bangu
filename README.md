#BANGU -- From Zero To One   盘古, 开天辟地

![](http://i.imgur.com/aFFeNV6.jpg)
This project is about smart ehouse which base on python, I use [Raspberry pi](https://www.raspberrypi.org/) to get senor data and GPIO to display message . Also it can be simply displayed on screen through a website which is based on Django.

You can contact me via email: 564326047@qq.com(wangqingbaidu) 

Or visit my blog  [www.wangqingbaidu.cn](http://www.wangqingbaidu.cn) for latest news.

Later I will display all the mother board and sensors which I have already used. This will help anyone who wants to implement by their own.

##Chinese
哒遛君最近蛋疼鼓捣了一个树莓派的小项目，是基于MVC的设计模式开发的，里面主要包括了几个模块。其中包含了很多哒遛君自己的apikey之类的东西，还望大家学习之余不要乱用。项目的注释写的还算清楚，而且采用的是MVC设计模式，Model复制数据库的存储，View负责前端展示目前使用了LED，lcd1602等，后面会添加web展示模块，Controller包括API数据拉取，Sensor数据获取等。源代码请转至我的github [https://github.com/wangqingbaidu/bangu](https://github.com/wangqingbaidu/bangu)。使用是非常简单的，install之后可以直接`service bangu start` 或者重启则开机启动。

###目前已有的功能
>1. 可以显示当天以及明天天气状况的led灯，这个天气预报是从API里面获取的。 
>2. 可以显示室内温湿度的lcd显示屏，这个模块需要dht11传感器，大家可以自行购买。 
>3. 添加了消息的推送，使用的是instapush这个应用，有ios以及Android版。 
>4. 实现了TTS转化功能（还没有加入到项目中，只是测试通过，可以调用，木有应用场景） 
>5. 实现发邮件的功能，可以根据订阅者的邮箱地址，定时发送邮件。 
>6. 把log功能进行了整合，如果那个模块有问题，不会出现宕机，而是会输出到log中。
>7. 添加基于Django的智能语音对话系统，访问树莓派ip，可以使用对应接口与树莓派语音聊天。

###哒遛君正准备添加的功能。
>1. 基于深度学习的人脸识别系统（正在开发，话说哒遛君就是这个的。。。） 
>2. 红外以及超声测距，感知附近的人。 
>3. 打卡模块（电容开关，还没有想到有啥鸟用。。。）

代码中的注释写的还算清楚吧，大家有不懂得可以去看代码，本人正在撰写相关的文档，相信不久就会有详细的介绍。 

项目依赖一些小的硬件，在bangu主页有介绍，但是可能不全。。。
 
使用也是非常的简单，直接安装就行，开机自动启动或者直接启动service（前提是各位大侠的插线十分准确）

配置文件都在[bangu.cfg](https://github.com/wangqingbaidu/bangu/blob/master/bangu.cfg)中其中city字段大家可以自行修改，其他的所有的gpio的pin都是board模式，大家可以修改也可以保持原样，但是bangu会自己检查这些设置。

好啦就说到这里吧，大家有什么问题可以去我的博客转转，获得最新的信息，也可以发送到我的邮箱564326047@qq.com。
期望能跟大家一起，玩转树莓派。

##News
>####1.	2016-11-27 Weather with LED completed!                                                          
>####2.	2016-12-12 LCD display indoor temperature and humidity completed!          
>####3.	2016-12-19 InstaPush added!   
>####4.	2016-12-23 Baidu Voice TTS,  Email module!
>####5.	2016-12-25 Log merge!
>####6.	2017-01-04 Timer scheduler.
>####7. 	2017-01-08 Add supports of another powerful message push app which is called [pushover](https://pushover.net/).
>####8.	2017-01-11 Transform Baidu API to others gradually.
>####9.	2017-01-17 Create documents on some moduler.
>####10. 2017-01-20 Use [http://tianqi.moji.com/](http://tianqi.moji.com/) as weather API which based on python reptile.   
>> See [Src code](https://github.com/wangqingbaidu/bangu/blob/master/utils/WeatherAPI.py) for details.

>####11. 2017-02-24 Baidu Audio to Text Service fixed.
>####12. 2017-02-24 New interaction with bangu.
>>Which is based on  [iflytek](http://www.xfyun.cn/) speech recognition and [tuling](http://www.tuling123.com/) robot. Feature bangu can be interacted  with voice.

>####13.  2017-2-28 Add BanguWeb which is based on Django.
>>One can chat with bangu by visiting bangu's ip. Use the given format  `$BANGUIP/api/chattingDisplay?info=Hello Bangu!`. Later I will develop an Android app for chatting.

![](http://i.imgur.com/30cNz9i.png)

##Hardware Required
#####Network connection is the most important.

>1.Raspberry pi 2 or later
>
>2.Some LED
>
>3.DHT11

>4.A piece of LCD1602
> 
>5.Loudspeaker
>
>6.Camera


##How to use?
Clone srouce code to your `Home`

`git clone https://github.com/wangqingbaidu/bangu.git`

`cd bangu`

####1. Install requirements
`pip install -r requirements.txt`

####2. Install bangu
bangu is very easy to install and auto run when Raspberry pi is reboot! Just one command to enjoy bangu, one thing you have to take care is that you should run the follow command in  `ROOT`

`python BANGUHOME/tools/bangu.py install && reboot`

##Default Bangu settings
All settings are in `BANGUHOME/bangu.cfg`

Board model and 11, 13, 15 pin is used to display Red, Green, Yellow

##Show


![](http://i.imgur.com/iKfpfMk.jpg)
