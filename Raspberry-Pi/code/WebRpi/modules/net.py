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
        personal = {
            'ip_v4': str(),
            'netmask_v4': str(),
            'broadcast_v4': str(),
            'ip_v6': str(),
            'netmask_v6': str(),
            'broadcast_v6': str(),
            'mac': str()
        }
        for data in datas:
            personal.update({'name': name})
            if data.family.name == 'AF_INET':
                personal.update({
                    'ip_v4':
                    data.address if data.address else str(),
                    'netmask_v4':
                    data.netmask if data.netmask else str(),
                    'broadcast_v4':
                    data.broadcast if data.broadcast else str()
                })
            elif data.family.name == 'AF_INET6':
                personal.update({
                    'ip_v6':
                    data.address.split('%')[0] if data.address else str(),
                    'netmask_v6':
                    data.netmask if data.netmask else str(),
                    'broadcast_v6':
                    data.broadcast if data.broadcast else str()
                })
            elif data.family.name == 'AF_PACKET':
                personal.update(
                    {'mac': data.address if data.address else str()})
        net_info.append(personal)

    return net_info


if __name__ == '__main__':
    net_info = get_net_info()
    print(net_info)
