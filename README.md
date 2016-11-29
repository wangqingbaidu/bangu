#bangu 盘古
##                --from zero to one 开天辟地 
##<font color=red>Weather with LED completed!</font>

This project is about smart ehouse which base on python, I use [Raspberry pi](https://www.raspberrypi.org/) to get senor data and GPIO to display message . Also it can be simply displayed on screen through a website which is based on Django.

You can contact me via email: 564326047@qq.com(wangqingbaidu) 

Or visit my blog  [www.wangqingbaidu.cn](http://www.wangqingbaidu.cn) for latest news.

###For business or industrialization please call (+86)13261527505, Mr. Zhang


Later I will display all the mother board and sensors which I have already used. This will help anyone who wants to implement by their own.

##Hardware Required
>1.Raspberry pi 2 or later
>
>2.Some LED

##How to use?
bangu is very easy to install and auto run when Raspberry pi is reboot!

Just one command to enjoy bangu, one thing you have to take care is that you should run the follow command in  `ROOT`

`python BANGUHOME/tools/bangu.py install && reboot`

##Default Bangu settings
All settings are in `BANGUHOME/bangu.cfg`

Board model and 11, 13, 15 pin is used to display Red, Green, Yellow
