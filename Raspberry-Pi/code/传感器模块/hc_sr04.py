#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: hc_sr04.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2020-11-01 17:51:48

Description: 超声波测距传感器模块HC-SR04
"""

import time

import RPi.GPIO as GPIO

Trig_Pin = 20
Echo_Pin = 21


def getDistance():
    """获取传感器数据
    :returns: TODO

    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo_Pin, GPIO.IN)
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 / 2


try:
    while True:
        dis = getDistance()
        print('Distance:%0.2f cm' % dis)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
