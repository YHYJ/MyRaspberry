# README

Raspberry Pi资料

---

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [Raspberry Pi OS](#raspberry-pi-os)
    * [系统下载](#系统下载)
    * [系统安装](#系统安装)
    * [项目](#项目)
* [Arch Linux ARM](#arch-linux-arm)
    * [系统下载](#系统下载-1)
    * [系统安装](#系统安装-1)

<!-- vim-markdown-toc -->

---

| 编号 | 镜像                                   | 架构  | 基础镜像      | 桌面环境 |
| ---  | ---                                    | ---   | ---           | ---      |
| 1    | ArchLinuxARM-rpi-aarch64-latest.tar.gz | arm64 | ArchLinuxARM  | 无       |
| 2    | ArchLinuxARM-rpi-4-latest.tar.gz       | armhf | ArchLinuxARM  | 无       |
| 3    | YY-MM-DD-raspios-buster-arm64-lite.zip | arm64 | Debian buster | 无       |
| 4    | YY-MM-DD-raspios-buster-arm64.zip      | arm64 | Debian buster | 有       |
| 5    | YY-MM-DD-raspios-buster-armhf-lite.zip | armhf | Debian buster | 无       |
| 6    | YY-MM-DD-raspios-buster-armhf.zip      | armhf | Debian buster | 有       |
| 7    | YY-MM-DD-raspios-buster-armhf-full.zip | armhf | Debian buster | 有       |

---

## Raspberry Pi OS

### 系统下载

[官方下载站](https://downloads.raspberrypi.org)
[64位系统](https://downloads.raspberrypi.org/raspios_arm64/images)
[64位lite系统](https://downloads.raspberrypi.org/raspios_lite_arm64/images)
[32位系统](https://downloads.raspberrypi.org/raspios_armhf/images)
[32位lite系统](https://downloads.raspberrypi.org/raspios_lite_armhf/images)
[32位full系统](https://downloads.raspberrypi.org/raspios_full_armhf/images)

### 系统安装

[官方 - 系统安装](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

dd安装：

```shell
dd bs=4M if=2020-08-20-raspios-buster-armhf.img of=/dev/sdX status=progress conv=fsync
```

### 项目

[官方 - 示例项目](https://projects.raspberrypi.org/zh-CN/projects)

## Arch Linux ARM

### 系统下载

[官方下载站](https://archlinuxarm.org/about/downloads)

### 系统安装

[Raspberry Pi 4 install Arch Linux ARM](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4#installation)