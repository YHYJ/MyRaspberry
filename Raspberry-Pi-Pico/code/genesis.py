#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: genesis.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2021-06-09 16:48:34

Description: LED灯闪烁并打印语句（包括随机数字前缀）
"""

import random

from machine import Pin, Timer

led = Pin(25, Pin.OUT)
timer = Timer()


def genesis(timer):
    led.toggle()
    print('{} - Hello world!'.format(random.randint(0, 100000000)))


timer.init(freq=5, mode=Timer.PERIODIC, callback=genesis)