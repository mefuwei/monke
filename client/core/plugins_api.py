#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
from client.plugins import cpu,memory,traffic,hard,load


def cpu_info():
    return cpu.monitor()


def load_info():
    return load.monitor()


def memory_info():
    return memory.monitor()


def traffic_info():

    return traffic.monitor()


def hard_info():
    return hard.collect()




