# Bangu详解（二）--- Tools安装脚本

## 一、`GetBanguHome.py`
这个脚本是用来安装到python目录的，用来获取寻找bangu的安装目录，默认会在当前目录上递归的寻找，直到碰到包含`Controller`, `Model`, `View`三个目录为止，表示着寻找到了根目录，如果寻找到`\`依然没有结果，就再寻找一次`/root/bangu`这个推荐安装目录。

当寻找到目录之后会将目录添加到`sys.path`, 

此模块包含一个`getHome()`方法，用来显示返回bangu目录。

这里各位大侠可能要问了为啥不使用 `export banguhome=balabala`，这个方法哒溜君试过，在用root用户使用的过程中是好使的，但是如果想弄成开机启动，这个`export`就不起作用了。囧。

## 二、`bangu.py`
#### <font color=red>请使用root用户执行脚本</font>

bangu的安装脚本，可以使用三个参数，分别是`install`,`start`,`stop`, 各位大侠可以根据需要自行选择，第一次使用bangu的时候一定要进行install，除非不care开机启动，如果install之后，使用`service bangu start/stop/restart`命令控制bangu的状态。

#### 1.install
a.安装bangu

```python
gethome_path = os.path.join(os.path.dirname(sys.argv[0]), 'GetBanguHome.py')
bashrc_path = os.environ['HOME'] + '/.bashrc' 
if not 'export BANGUHOME=' + bangu_home in bashrc:
    os.system('echo "{0}" >> {1} && source {1}'.format('export BANGUHOME=' + bangu_home, bashrc_path))
    ```

将`GetBanguHome.py`添加到系统目录，同时将此目录`export`到`~/.bashrc`

b.bangu开机启动

```powershell
#!/bin/sh
### BEGIN INIT INFO
# Provides:          wangqingbaidu@bangu
# Required-Start:    $remote_fs $network
# Required-Stop:     $remote_fs $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start or stop bangu.
### END INIT INFO
case $1 in
    start)
        python {0} {1}
        ;;
    stop)
        python {0} {2}
        ;;
*)
echo "Usage: $0 (start|stop)"
;;
esac
```

c.one  more thing

>剩下的操作就是初始化数据库，并且询问是否重新启动树莓派。

#### 2.start
这个指令里面包括了bangu所支持的所有的功能模块，各位大侠可以按需开启。

```python
thread.start_new_thread(ThreadUpdateWeather2DB, (600,))
thread.start_new_thread(ThreadWeatherLEDFlicker, tuple())
thread.start_new_thread(ThreadIndoorTmpHum2DB, (10,))
thread.start_new_thread(ThreadLCDTemperatureHumidity, tuple())
thread.start_new_thread(ThreadPushMessage2Phone, ([('23:00:00', '%H:%M:%S')],))
thread.start_new_thread(ThreadAudioAccessToken2DB, (999999,))
```

第一个是更新天气线程。

第二个是根据天气状况的LED闪烁。雨雪闪烁红色，霾，雾闪烁黄色，其它绿色。

第三个是更新室内温湿度线程。

第四个是[LCD1602](http://www.wangqingbaidu.cn/article/raspi1484039212.html)显示温湿度线程。

第五个是向手机推送消息线程。

第六个是更新百度TTS API token线程。

#### 3.stop
停止bangu运行，通过`ps -ef`获得bangu的pid，然后使用`killall`指令杀掉指定的pid。

[https://github.com/wangqingbaidu/bangu/blob/master/tools/bangu.py](https://github.com/wangqingbaidu/bangu/blob/master/tools/bangu.py)
### ☛[Bangu 地址](https://github.com/wangqingbaidu/bangu/)☚
