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

from modules.ups import output2web

app = Flask(__name__)


@app.route('/')
def index():
    """Flask Main"""
    return render_template('index.html')


@app.route('/update/ups', methods=['GTE', 'POST'])
def test():
    """Flask Main"""
    ups = output2web() # UPS数据

    ajax = dict()
    ajax['ups'] = ups
    return json.dumps(ajax)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=80)
