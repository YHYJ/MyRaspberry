#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: ups.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-28 10:11:54

Description: 树莓派UPS-18650 Lite模块检测程序

UPS-18650 Lite v1.0版本中，插入电源时GPIO是高电平
UPS-18650 Lite v1.1版本中，插入电源时GPIO是低电平

1. `i2cdetect -l`命令查看Pi采用的是哪个i2c总线（带有'bcm'关键字的，假设为1）
2. `i2cdetect -y 1`命令查看编号为1的i2c总线上挂载的设备地址（这里是0x36）
"""

import struct
import time

import RPi.GPIO as gpio
import smbus

address = 0x36


def read_capacity(bus):
    """读取电池剩余容量"""
    resp = bus.read_word_data(address, 0x04)
    swapped = struct.unpack('<H', struct.pack('>H', resp))[0]
    capacity = swapped / 256
    return capacity


def read_voltage(bus):
    """读取电池电压"""
    resp = bus.read_word_data(address, 0x02)
    swapped = struct.unpack('<H', struct.pack('>H', resp))[0]
    voltage = swapped * 1.25 / 1000 / 16
    return voltage


def QuickStart(bus):
    bus.write_word_data(address, 0x06, 0x4000)


def PowerOnReset(bus):
    bus.write_word_data(address, 0xfe, 0x0054)


def output2stdout():
    """本地输出"""
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(4, gpio.IN)

    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
    bus = smbus.SMBus(1)

    print('Initialize the MAX17040 ......')

    if (gpio.input(4) == gpio.HIGH):
        PowerOnReset(bus)

    while True:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        voltage = read_voltage(bus)
        capacity = read_capacity(bus)

        if capacity >= 100 and gpio.input(4) == gpio.LOW:
            print('\r\033[?25l{} {} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.
                  format(now, '🔌', voltage, capacity, 'Battery Full'),
                  end='',
                  flush=True)
        elif capacity >= 100 and gpio.input(4) == gpio.HIGH:
            print('\r\033[?25l{} {} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.
                  format(now, '🔋', voltage, capacity, 'Battery Full'),
                  end='',
                  flush=True)
        elif 10 < capacity < 100 and gpio.input(4) == gpio.LOW:
            print('\r\033[?25l{} {} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.
                  format(now, '🔌', voltage, capacity, 'Battery Charging'),
                  end='',
                  flush=True)
        elif 10 < capacity < 100 and gpio.input(4) == gpio.HIGH:
            print('\r\033[?25l{} {} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.
                  format(now, '🔋', voltage, capacity, 'Battery Discharging'),
                  end='',
                  flush=True)
        elif 0 < capacity <= 10 and gpio.input(4) == gpio.LOW:
            print('\r\033[?25l{} {} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.
                  format(now, '🔌', voltage, capacity, 'Battery Low'),
                  end='',
                  flush=True)
        elif 0 < capacity <= 10 and gpio.input(4) == gpio.HIGH:
            print('\r\033[?25l{} {} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.
                  format(now, '🔋', voltage, capacity, 'Battery Low'),
                  end='',
                  flush=True)
        else:
            print(
                '\r\033[?25l{} Battery: {:.2f}V | {:.2f}% | {}\033[0m'.format(
                    now, voltage, capacity, 'Battery Unknown'),
                end='',
                flush=True)
        time.sleep(2)


def output2web():
    """输出到Web"""
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(4, gpio.IN)

    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
    bus = smbus.SMBus(1)

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    voltage = read_voltage(bus)
    capacity = read_capacity(bus)

    if capacity >= 100 and gpio.input(4) == gpio.LOW:
        info = '{} {} {}: {:.2f}V | {:.2f}%'.format(now, '🔌', 'Battery Full',
                                                    voltage, capacity)
    elif capacity >= 100 and gpio.input(4) == gpio.HIGH:
        info = '{} {} {}: {:.2f}V | {:.2f}%'.format(now, '🔋', 'Battery Full',
                                                    voltage, capacity)
    elif 10 < capacity < 100 and gpio.input(4) == gpio.LOW:
        info = '{} {} {}: {:.2f}V | {:.2f}%'.format(now, '🔌',
                                                    'Battery Charging',
                                                    voltage, capacity)
    elif 10 < capacity < 100 and gpio.input(4) == gpio.HIGH:
        info = '{} {} {}: {:.2f}V | {:.2f}%'.format(now, '🔋',
                                                    'Battery Discharging',
                                                    voltage, capacity)
    elif 0 < capacity <= 10 and gpio.input(4) == gpio.LOW:
        info = '{} {} {}: {:.2f}V | {:.2f}%'.format(now, '🔌', 'Battery Low',
                                                    voltage, capacity)
    elif 0 < capacity <= 10 and gpio.input(4) == gpio.HIGH:
        info = '{} {} {}: {:.2f}V | {:.2f}%'.format(now, '🔋', 'Battery Low',
                                                    voltage, capacity)
    else:
        info = '{} {}: {:.2f}V | {:.2f}% | {}'.format(now, 'Battery Unknown',
                                                      voltage, capacity)

    return info


if __name__ == '__main__':
    output2stdout()
