#!/usr/bin/env bash

: << !
Name: create-favicon.sh
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2023-04-04 11:10:05

Description: 原始favicon文件夹命名格式为"favicon_logosc.X"，其中'X'是数字

Attentions:
-

Depends:
-
!

if [[ -d static ]]; then
  cd static || exit 1
elif [[ -d ../static ]]; then
  cd ../static || exit 1
else
  echo -e "'static' folder not found"
  exit 1
fi

if [[ -d favicon_logosc.$1 ]]; then
  rm -rf favicon
  ln -s favicon_logosc."$1" favicon
else
  echo -e "'favicon_logosc.$1' folder not found"
  exit 1
fi
