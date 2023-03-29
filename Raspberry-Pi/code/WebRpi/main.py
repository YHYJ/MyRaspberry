#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: main.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-28 16:41:54

Description:
"""

from flask import Flask
from waitress import serve

from modules.ups import output2web

app = Flask(__name__)


@app.route('/')
def main():
    """Flask Main"""
    ups = output2web()
    return ups


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=80)
