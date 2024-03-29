#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: disk.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-31 14:52:10

Description: 磁盘监控
"""

import psutil


def get_disk_info():
    """获取磁盘信息"""
    disk_path = '/'
    diskinfo= psutil.disk_usage(path=disk_path)

    factor = 3  # 返回值单位是byte，factor = 3/2/1分别是将单位转为GB/MB/KB
    muse = 1024**factor
    digit = 1  # 结果精确度（保留多少位小数）

    disk_root = dict()
    disk_root['path'] = disk_path
    disk_root['total'] = round(diskinfo[0] / muse, digit)
    disk_root['used'] = round(diskinfo[1] / muse, digit)
    disk_root['free'] = round(diskinfo[2] / muse, digit)
    disk_root['percent'] = round(diskinfo[3], digit)

    disk_info = list()
    disk_info.append(disk_root)

    return disk_info


if __name__ == '__main__':
    disk_info = get_disk_info()
    print(disk_info)
