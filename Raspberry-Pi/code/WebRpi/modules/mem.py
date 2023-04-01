#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: mem.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-31 11:46:45

Description: 内存监控
"""

import psutil


def get_mem_info():
    """获取内存信息"""
    vmeminfo = psutil.virtual_memory()

    factor = 2  # 返回值单位是byte，factor = 3/2/1分别是将单位转为GB/MB/KB
    muse = 1024**factor
    digit = 0  # 结果精确度（保留多少位小数）

    mem_info = dict()
    mem_info['total'] = round(vmeminfo[0] / muse, digit)
    mem_info['available'] = round(vmeminfo[1] / muse, digit)
    mem_info['percent'] = round(vmeminfo[2], digit)
    mem_info['used'] = round(vmeminfo[3] / muse, digit)
    mem_info['free'] = round(vmeminfo[4] / muse, digit)
    mem_info['active'] = round(vmeminfo[5] / muse, digit)
    mem_info['inactive'] = round(vmeminfo[6] / muse, digit)
    mem_info['buffers'] = round(vmeminfo[7] / muse, digit)
    mem_info['cached'] = round(vmeminfo[8] / muse, digit)
    mem_info['shared'] = round(vmeminfo[9] / muse, digit)
    mem_info['slab'] = round(vmeminfo[10] / muse, digit)

    return mem_info


if __name__ == '__main__':
    mem_info = get_mem_info()
    print(mem_info)
