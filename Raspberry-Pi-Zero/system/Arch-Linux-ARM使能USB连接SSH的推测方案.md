# Arch-Linux-ARM使能USB连接SSH的推测方案

<!-- File: Arch-Linux-ARM使能USB连接SSH的推测方案.md -->
<!-- Auther: YJ -->
<!-- Email: yj1516268@outlook.com -->
<!-- Created Time: 2021-07-02 16:26:36 -->

---

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [image](#image)
* [boot](#boot)
* [avahi](#avahi)

<!-- vim-markdown-toc -->

---

<!-- Object info -->

---

## image

1. 使用专为ARMv6 Raspberry发布的镜像ArchLinuxARM-rpi-latest.tar.gz
2. 参照[Raspberry Pi](https://archlinuxarm.org/platforms/armv6/raspberry-pi)进行安装

## boot

1. 修改`/boot/cmdline.txt`，在'rootwait'后新增'modules-load=dwc2,g_ether'参数
2. 修改`/boot/config.txt`，在最后新增'dtoverlay=dwc2'行

## avahi

1. `pacman -S avahi`
2. `systemctl disable systemd-resolved`
3. `systemctl enable avahi-daemon`
