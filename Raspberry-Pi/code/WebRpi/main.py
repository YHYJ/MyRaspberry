#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: main.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-28 16:41:54

Description:
"""

import json

from flask import Flask, render_template
from waitress import serve

from modules.cpu import get_cpu_info
from modules.disk import get_disk_info
from modules.mem import get_mem_info
from modules.net import get_net_info
from modules.swap import get_swap_info
from modules.sys import get_sys_info
from modules.ups import get_ups_info
from modules.user import get_user_info

app = Flask(__name__)


@app.route('/')
def index():
    """Flask Main"""
    return render_template('index.html')


@app.route('/update/ups')
def ups():
    """Update UPS info"""
    ajax = dict()
    ajax['ups'] = get_ups_info()
    return json.dumps(ajax)


@app.route('/update/sys')
def sys():
    """Update System info"""
    ajax = dict()
    ajax['sys'] = get_sys_info()
    return json.dumps(ajax)


@app.route('/update/user')
def user():
    """Update User info"""
    ajax = dict()
    ajax['user'] = get_user_info()
    return json.dumps(ajax)


@app.route('/update/cpu')
def cpu():
    """Update CPU info"""
    ajax = dict()
    ajax['cpu'] = get_cpu_info()
    return json.dumps(ajax)


@app.route('/update/mem')
def mem():
    """Update Memory info"""
    ajax = dict()
    ajax['mem'] = get_mem_info()
    return json.dumps(ajax)


@app.route('/update/swap')
def swap():
    """Update Swap info"""
    ajax = dict()
    ajax['swap'] = get_swap_info()
    return json.dumps(ajax)


@app.route('/update/disk')
def disk():
    """Update Disk info"""
    ajax = dict()
    ajax['disk'] = get_disk_info()
    return json.dumps(ajax)


@app.route('/update/net')
def net():
    """Update Net info"""
    ajax = dict()
    ajax['net'] = get_net_info()
    return json.dumps(ajax)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=80)
