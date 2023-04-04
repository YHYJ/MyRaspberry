#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: sys.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-04-02 23:43:17

Description: 系统监控
"""

from datetime import datetime
import platform

import psutil


def get_sys_info():
    """获取系统信息"""
    uname = platform.uname()
    machine = '{}{}'.format(uname[4][0].title(), uname[4][1:].title())
    architecture = platform.architecture()
    boot_ts = psutil.boot_time()
    now_ts = datetime.now()
    boot_time = datetime.strftime(datetime.fromtimestamp(boot_ts),
                                  "%Y-%m-%d %H:%M:%S")
    run_time = str(now_ts - datetime.fromtimestamp(boot_ts))

    sys_data = dict()
    sys_data['system'] = uname[0]
    sys_data['hostname'] = uname[1]
    sys_data['kernel'] = uname[2]
    sys_data['machine'] = machine
    sys_data['arch'] = architecture[0]
    sys_data['boot_time'] = boot_time
    sys_data['run_time'] = run_time

    sys_info = list()
    sys_info.append(sys_data)

    return sys_info


if __name__ == '__main__':
    sys_info = get_sys_info()
    print(sys_info)
