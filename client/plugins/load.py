#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W


import os
def monitor():
    """
    :Return a dictionary, including load_1,load_5,load_15
    """
    command = "uptime"
    result  = ((os.popen(command).read()).strip()).split(':')[-1]
    load_list =  result.split(',')
    load_1,load_5,load_15 = float(load_list[0]),float(load_list[1]),float(load_list[2])

    load_avg = {
        "load_1" : load_1,
        "load_5" : load_5,
        "load_15" : load_15
    }

    return load_avg


