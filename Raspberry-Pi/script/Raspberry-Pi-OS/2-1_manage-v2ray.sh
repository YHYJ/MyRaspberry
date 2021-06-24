#!/usr/bin/env bash

: << !
Name: 2-1_manage-v2ray.sh
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2021-06-24 10:55:41

Description: 安装V2Ray

Attentions:
- 因为软件源里没有v2ray包，使用官方脚本手动安装
- 该安装脚本不会自动生成配置文件

Depends:
-
!

####################################################################
#+++++++++++++++++++++++++ Define Variable ++++++++++++++++++++++++#
####################################################################
#------------------------- Program Variable
# program name
name=$(basename "$0")
readonly name
# program version
readonly major_version=0.1
readonly minor_version=20210624
readonly rel_version=1

#------------------------- Exit Code Variable
readonly normal=0           # 一切正常
readonly err_file=1         # 文件/路径类错误
readonly err_param=2        # 参数错误
readonly err_fetch=48       # checkupdate错误
readonly err_permission=110 # 权限错误
readonly err_range=122      # 取值范围错误
readonly err_ctrl_c=130     # 接收到INT(Ctrl+C)指令
readonly err_unknown=255    # 未知错误
readonly err_no_program=127 # 未找到命令

#------------------------- Parameter Variable
# description variable
readonly desc="TODO"

####################################################################
#+++++++++++++++++++++++++ Define Function ++++++++++++++++++++++++#
####################################################################
#------------------------- Info Function
function helpInfo() {
  echo -e ""
  echo -e "\e[32m$name\e[0m\e[1m$desc\e[0m"
  echo -e "--------------------------------------------------"
  echo -e "Usage:"
  echo -e ""
  echo -e "     $name [OPTION]"
  echo -e ""
  echo -e "Options:"
  echo -e "     -i, --install     安装V2Ray"
  echo -e "     -u, --update      更新V2Ray"
  echo -e "     -r, --remove      卸载V2Ray"
  echo -e ""
  echo -e "     -h, --help        显示帮助信息"
  echo -e "     -v, --version     显示版本信息"
}

function versionInfo() {
  echo -e "\e[1m$name\e[0m version (\e[1m$major_version-$minor_version.$rel_version\e[0m)"
}
#------------------------- Feature Function

####################################################################
#++++++++++++++++++++++++++++++ Main ++++++++++++++++++++++++++++++#
####################################################################
if [[ -n $1 ]]; then
  case $1 in
    -i | --install)
      # 安装可执行文件和 .dat 数据文件
      bash .fhs-install-v2ray/install-release.sh
      ;;
    -u | --update)
      # 更新可执行文件和 .dat 数据文件
      bash .fhs-install-v2ray/install-release.sh
      bash .fhs-install-v2ray/install-dat-release.sh
      ;;
    -r | --remove)
      # 移除V2Ray
      bash .fhs-install-v2ray/install-release.sh --remove
      ;;
    -h | --help)
      helpInfo
      exit $normal
      ;;
    -v | --version)
      versionInfo
      exit $normal
      ;;
    *)
      helpInfo
      exit $err_unknown
      ;;
  esac
else
  echo -e 'TODO'
fi
