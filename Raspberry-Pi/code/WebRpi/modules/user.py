#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: user.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-04-03 00:57:31

Description: 用户监控
"""

from datetime import datetime

import psutil


def get_user_info():
    """获取用户信息"""
    users = psutil.users()

    user_info = list()
    for user in users:
        personal = dict()
        started = datetime.strftime(datetime.fromtimestamp(user[3]),
                                    "%Y-%m-%d %H:%M:%S")
        personal.update({
            'name': user[0],
            'terminal': user[1],
            'host': user[2],
            'started': started
        })
        user_info.append(personal)

    return user_info


if __name__ == '__main__':
    user_info = get_user_info()
    print(user_info)
