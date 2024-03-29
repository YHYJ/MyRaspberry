#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: swap.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-31 14:42:38

Description: 交换分区监控
"""

import psutil


def get_swap_info():
    """获取内存信息"""
    smeminfo = psutil.swap_memory()

    factor = 2  # 返回值单位是byte，factor = 3/2/1分别是将单位转为GB/MB/KB
    muse = 1024**factor
    digit = 0  # 结果精确度（保留多少位小数）

    swap_data = dict()
    swap_data['total'] = round(smeminfo[0] / muse, digit)
    swap_data['used'] = round(smeminfo[1] / muse, digit)
    swap_data['free'] = round(smeminfo[2] / muse, digit)
    swap_data['percent'] = round(smeminfo[3], digit)
    swap_data['sin'] = round(smeminfo[4] / muse, digit)
    swap_data['sout'] = round(smeminfo[5] / muse, digit)

    swap_info = list()
    swap_info.append(swap_data)

    return swap_info


if __name__ == '__main__':
    swap_info = get_swap_info()
    print(swap_info)
