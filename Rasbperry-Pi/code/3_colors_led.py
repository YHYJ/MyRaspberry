#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: 3_colors_led.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2020-11-01 18:21:01

Description: 3色LED灯
"""

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

R, G, B = 6, 13, 5

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

pwmR = GPIO.PWM(R, 70)
pwmG = GPIO.PWM(G, 70)
pwmB = GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

t = 0.4
for i in range(5):

    print("loop " + (i + 1).__str__() + "/5")

    # 红色灯全亮，蓝灯，绿灯全暗（红色）
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(100)
    time.sleep(t)

    # 绿色灯全亮，红灯，蓝灯全暗（绿色）
    pwmR.ChangeDutyCycle(100)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(100)
    time.sleep(t)

    # 蓝色灯全亮，红灯，绿灯全暗（蓝色）
    pwmR.ChangeDutyCycle(100)
    pwmG.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)

    # 红灯，绿灯全亮，蓝灯全暗（黄色）
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(100)
    time.sleep(t)

    # 红灯，蓝灯全亮，绿灯全暗（洋红色）
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)

    # 绿灯，蓝灯全亮，红灯全暗（青色）
    pwmR.ChangeDutyCycle(100)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)

    # 红灯，绿灯，蓝灯全亮（白色）
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)

    # 调整红绿蓝LED的各个颜色的亮度组合出各种颜色
    for i in range(0, 101, 1):
        pwmR.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(100, -1, -1):
        pwmR.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(0, 101, 1):
        pwmG.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(100, -1, -1):
        pwmG.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(0, 101, 1):
        pwmB.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(100, -1, -1):
        pwmB.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(0, 101, 1):
        pwmB.ChangeDutyCycle(i)
        pwmG.ChangeDutyCycle(i)
        pwmR.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(100, -1, -1):
        pwmB.ChangeDutyCycle(i)
        pwmG.ChangeDutyCycle(i)
        pwmR.ChangeDutyCycle(i)
        time.sleep(0.02)

pwmR.stop()
pwmG.stop()
pwmB.stop()

GPIO.cleanup()
