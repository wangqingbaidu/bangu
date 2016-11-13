# -*- coding: UTF-8 -*- 
'''
View.Hardware.RaspGPIO is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from utils.ReadConfig import BanguConfig

class RaspGPIO:
    """
    This class is used to initialize GPIO settings.
    Parameters
    -------------
    @model: Rasp board model which GPIO number stands for, can be GPIO.BOARD or GPIO.BCM
    @pins: Which pin is to be used in this project.
    """
    def __init__(self,
                 model = 'board',
                 pins = BanguConfig().get_pins_settings()):
        
        self.__Define_GPIO_model(model)            
        self.__Define_GPIO_pin(pins)
        
    def __Define_GPIO_model(self, model):       
#       If model is not GPIO.BOARD or GPIO.BCM, set it to GPIO.BOARD.
        model = model.upper()
        if model in ['BOARD', 'BCM']:
            self.model = model
        else:
            self.model = 'BOARD'
        
        if self.model == 'BOARD':
            GPIO.setmode(GPIO.BOARD)
        else:
            GPIO.setmode(GPIO.BCM)        

    def __Define_GPIO_pin(self, pins):
#       GPIO pins type define.
        pin_map = {'out': GPIO.OUT, 'in': GPIO.IN}
        if not type(pins) is dict:
            self.pins = None
        else:
            del_keys = []
            for pin in pins.keys():
                if 0 < pin <= 40 and pin_map.has_key(pins[pin].lower()):
                    pins[pin] = pins[pin].lower()
                    GPIO.setup(int(pin), pin_map[pins[pin]])
                else:
                    del_keys.append(pin)
#           Delete extra keys
            for del_key in del_keys:
                del pins[del_key]
            
            self.pins = pins
            
    def set_GPIO_pin(self, pins):
        self.__Define_GPIO_pin(pins)
    
    def get_GPIO_pin(self):
        return self.pins
    
    def pin_set_heigh(self, pin):
        if self.pins.has_key(pin):
            if self.pins[pin] == 'out':
                GPIO.output(pin, GPIO.HIGH)
            else:
                print 'GPIO model %s pin %d is not %s.' %(self.model, pin, 'GPIO.OUT')
        else:            
            print 'GPIO model %s pin %d is not defined!' %(self.model, pin, 'GPIO.OUT')
                
    def pin_set_low(self, pin):
        if self.pins.has_key(pin):
            if self.pins[pin] == 'out':
                GPIO.output(pin, GPIO.LOW)
            else:
                print 'GPIO model %s pin %d is not %s.' %(self.model, pin, 'GPIO.OUT')
        else:            
            print 'GPIO model %s pin %d is not defined!' %(self.model, pin)
                
    def pin_get_in(self, pin):
        if self.pins.has_key(pin):
            if self.pins[pin] == 'in':
                return GPIO.input(pin)
            else:
                print 'GPIO model %s pin %d is not %s.' %(self.model, pin, 'GPIO.IN')
        else:            
            print 'GPIO model %s pin %d is not defined!' %(self.model, pin)
            

raspgpio = RaspGPIO()