# 1-连接Pico

<!-- File: 1-连接Pico.md -->
<!-- Author: YJ -->
<!-- Email: yj1516268@outlook.com -->
<!-- Created Time: 2021-06-10 11:36:30 -->

---

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [1. 通过USB连接到MicroPython REPL](#1-通过usb连接到micropython-repl)
* [2. 通过UART连接到MicroPython REPL](#2-通过uart连接到micropython-repl)

<!-- vim-markdown-toc -->

---

官方文档提供的两个固件（blink和MicroPython）只有MicroPython会打开REPL供外部与固件进行通信

---

## 1. 通过USB连接到MicroPython REPL

1. 安装minicom

2. 执行以下命令：

    ```shell
    minicom -o -D /dev/ttyACM0
    ```

    > 其中：
    >
    > `-o`参数表示仅连接
    >
    > `-D`参数指定MicroPython的USB虚拟串行端口名
    >
    > 虚拟串行端口不必指定波特率

3. minicom连接到REPL之后可以使用'ctrl+d'快捷键重启MicroPython，重启完成后会打印固件信息

4. 在minicom中先按一次'ctrl+a'再按'z'即可调出帮助信息

## 2. 通过UART连接到MicroPython REPL

默认情况下Pico（RP2040芯片）的MicroPython不会在UART暴露REPL，只能在源文件`ports/rp2/mpconfigport.h`中修改此默认值后手动构建MicroPython才能允许通过UART连接REPL：

1. 修改`ports/rp2/mpconfigport.h`中的`MICROPY_HW_ENABLE_UART_REPL`值为1
2. 构建MicroPython固件

> 详见'raspberry-pi-pico-python-sdk.pdf'文档的2.2节
