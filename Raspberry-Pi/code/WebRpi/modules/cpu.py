#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: cpu.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-31 11:03:45

Description: CPU监控
"""

import psutil


def get_cpu_info():
    """获取CPU信息"""
    # 以interval前后的CPU时间为基准进行比较，为0则以上次调用以来的CPU时间为基准
    # 为true则返回每个CPU利用率的列表，为false则返回CPU总利用率
    cpu_percent = psutil.cpu_percent(interval=0, percpu=False)  # CPU使用率
    cpu_core_count = psutil.cpu_count(logical=False)  # CPU内核数
    cpu_thread_count = psutil.cpu_count(logical=True)  # CPU线程数
    cpu_load_1, cpu_load_5, cpu_load_10 = psutil.getloadavg() # CPU负载（1分钟、5分钟、10分钟）

    cpu_info = dict()
    cpu_info['percent'] = cpu_percent
    cpu_info['load_1'] = cpu_load_1
    cpu_info['load_5'] = cpu_load_5
    cpu_info['load_10'] = cpu_load_10
    cpu_info['core'] = cpu_core_count
    cpu_info['thread'] = cpu_thread_count

    return cpu_info


if __name__ == '__main__':
    cpu_info = get_cpu_info()
    print(cpu_info)
