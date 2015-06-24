#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
from os import popen


def monitor():
    """

    :return a dict including memtotal,%used
    """
    cmd ="sar -r 1 3|awk 'END {print}'"
    command = "cat /proc/meminfo |grep MemTotal|awk -F' ' '{print $2}'"
    memTotal_f = round(float(popen(command).read())/1024/1000,0)

    result = popen(cmd).read().split()
    if result and memTotal_f:
        used = float(result[3])
        memTotal = int(memTotal_f)
        memory = {
            "used" : used,
            "memtotal" :memTotal
        }
    else:

        memory =None
        print """error:
    please check the command 'sar',
    install :yum install sysstat,sudo apt-get install sysstat
        """

    return memory

