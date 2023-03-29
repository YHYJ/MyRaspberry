#!/usr/bin/env bash

: << !
Name: 1-2_apt-cleaner.sh
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-03-22 14:25:02

Description: 清除已卸载软件包的残留配置文件

Attentions:
-

Depends:
-
!

dpkg -l | rg '^rc' | awk '{print $2}' | xargs apt purge -y
