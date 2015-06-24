#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
import psutil

import os
def get_ip(addr="eth0"):
    """
    传递一个网卡名称获取ＩＰ
    默认获取eth0 的ＩＰ地址
    返回一个字典
    """
    net_addr = {}
    addr_dict = psutil.net_if_addrs()
    for inet, ip in addr_dict.items():
        if inet == addr:
            net_addr[inet] = ip[0][1]
    return net_addr

def get_hostname():
    hostname = os.popen("hostname -f").read()
    return hostname