#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from RaspGPIO import raspgpio
from utils.ReadConfig import configurations

class LCD1602:
    def __init__(self, pin_rs=21, pin_e=20, pins_db=[16, 7, 8, 25]):
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
        self.clear()
    def clear(self):
        """ Blank / Reset LCD """
        self.cmd(0x28)
        self.cmd(0x28) # $28 8-bit mode
        self.cmd(0x0c) # $0C 8-bit mode
        self.cmd(0x01) # $01 8-bit mode

    def cmd(self, bits, char_mode=False):
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
        raspgpio.pin_set_low(self.pin_e)

    def message(self, text):
        """ Send string to LCD. Newline wraps to second line"""
        for char in text:
            if char == '\n':
                self.cmd(0xC0) # next line
            else:
                self.cmd(ord(char),True)

lcd = LCD1602()
if __name__ == '__main__':    
    lcd = LCD1602()
    i = 1
    while (1):
        lcd.clear()
        msg = "Program  Running\n" + str(i) + " seconds"
        lcd.message(msg)    
        sleep(1 - len(msg) * 0.002)
        i += 1
        