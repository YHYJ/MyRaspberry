#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: net.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-31 15:05:26

Description: 网卡监控
"""

import psutil


def get_net_info():
    """获取网卡信息"""
    netinfo = psutil.net_if_addrs()

    net_info = list()
    for name, datas in netinfo.items():
        cache = dict()
        for data in datas:
            cache.update({'name': name})
            if data.family.name == 'AF_INET':
                cache.update({
                    'ip_v4': data.address,
                    'netmask_v4': data.netmask,
                    'broadcast_v4': data.broadcast
                })
            elif data.family.name == 'AF_INET6':
                cache.update({
                    'ip_v6': data.address,
                    'netmask_v6': data.netmask,
                    'broadcast_v6': data.broadcast
                })
            elif data.family.name == 'AF_PACKET':
                cache.update({'mac': data.address})
        net_info.append(cache)

    return net_info


if __name__ == '__main__':
    net_info = get_net_info()
    print(net_info)
