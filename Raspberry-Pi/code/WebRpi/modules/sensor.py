#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: sensor.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-04-04 14:08:14

Description: 传感器监控
"""

import psutil


def get_sensor_info():
    """获取传感器信"""
    """
    {'cpu_thermal':
        [shwtemp(label='', current=42.842, high=110.0, critical=110.0)]
    }
    """
    temperatures = psutil.sensors_temperatures()

    sensor_info = list()
    for name, datas in temperatures.items():
        personal = dict()
        for data in datas:
            personal.update({
                'name': name,
                'current': data.current,
                'high': data.high,
                'critical': data.critical
            })
        sensor_info.append(personal)

    return sensor_info


if __name__ == "__main__":
    sensor_info = get_sensor_info()
    print(sensor_info)
