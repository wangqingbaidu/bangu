#Bangu详解（一）----驱动LCD1602液晶显示屏

##一、材料准备
>1. 树莓派2 or later
>2. LCD1602
>3. 杜邦线若干

##二、代码详解
####<font color=red>本文的引脚都指的是树莓派的Board model的引脚。</font>
>1.初始化代码
><pre class="brush:python;">def __init__(self, pin_rs=21, pin_e=20, pins_db=[16, 7, 8, 25]):
    self.pin_rs = pin_rs
    self.pin_e = pin_e
    self.pins_db = pins_db
    cfg = configurations.get_lcd_pin_settings()
    try:
        self.pin_rs = cfg['rs']
        self.pin_e = cfg['e']
        self.pins_db = [cfg['bit4'], cfg['bit3'], cfg['bit2'], cfg['bit1']]
    except:
        pass
    self.clear() </pre>

>首先来看这里面的参数`pin_rs`,与`pin_e`分别代表lcd1602的两个功能引脚，这这两个针脚负责控制数据的输入，然后是四个数据引脚，由于lcd1602有2种工作模式，由于树莓派的GPIO引脚个数有限，所以这里采用了4bit引脚循环输入模式，这四个引脚分别对应于数据的从高到低的4个bit，lcd1602还有5个引脚，分别是vcc，vdd，v0，A,，K，前两个为电源的正负极，A，K为背光，V0用于调节显示数据的对比度，可以使用一个10k的电阻，可以使用滑动变阻器进行动态调节，这里就不再赘述。

>这里哒溜君增加了一句`cfg = configurations.get_lcd_pin_settings()`这个使用[bangu](https://github.com/wangqingbaidu/bangu/)的默认设置中进行读取，各位大小如果单独调试可以忽略。

>2.数据输送指令
>
><pre class="brush:python;">def cmd(self, bits, char_mode=False):
    """ Send command to LCD """
    sleep(0.002)
    bits=bin(bits)[2:].zfill(8)
    if char_mode == True:
        raspgpio.pin_set_heigh(self.pin_rs)
    else:
        raspgpio.pin_set_low(self.pin_rs)
    for pin in self.pins_db:
        raspgpio.pin_set_low(pin)
    for i in range(4):
        if bits[i] == "1":
            raspgpio.pin_set_heigh(self.pins_db[::-1][i])
    raspgpio.pin_set_heigh(self.pin_e)
    raspgpio.pin_set_low(self.pin_e)
    for pin in self.pins_db:
        raspgpio.pin_set_low(pin)
    for i in range(4,8):
        if bits[i] == "1":
            raspgpio.pin_set_heigh(self.pins_db[::-1][i-4])           
    raspgpio.pin_set_heigh(self.pin_e)
    raspgpio.pin_set_low(self.pin_e) </pre>

>这里遵循的就是lcd1602的标准驱动，大家可以参考[http://www.51hei.com/mcu/4327.html](http://www.51hei.com/mcu/4327.html)

>3.显示，清除
><pre class="brush:python;">def clear(self):
    """ Blank / Reset LCD """
    self.cmd(0x28)
    self.cmd(0x28) # $28 8-bit mode
    self.cmd(0x0c) # $0C 8-bit mode
    self.cmd(0x01) # $01 8-bit mode
def message(self, text):
    """ Send string to LCD. Newline wraps to second line"""
    self.clear()
    for char in text:
        if char == '\n':
            self.cmd(0xC0) # next line
        else:
            self.cmd(ord(char),True)</pre>

>这里哒溜君要提醒各位大侠的是，text一定要注意换行，因为lcd1602每行最多显示16个字符。

>最后给大家整份lcd1602的代码连接，建议结合bangu项目进行测试。

[https://github.com/wangqingbaidu/bangu/blob/master/View/Hardware/lcd1602.py](https://github.com/wangqingbaidu/bangu/blob/master/View/Hardware/lcd1602.py)
