#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W


from os import popen


def monitor():


    cmd = "sar -n DEV 1 4|grep ':'"
    result = popen(cmd).readlines()
    if result:
        traffic = {}
        for each in result:
            List = each.split()
            if List[1] != "lo" and List[1] != "IFACE":
                index = List[1]
                traffic[index] = {"into":List[4],
                           "out":List[5]
                           }
    else:
        print "error:execute 'sar' faild"
        traffic = None

    return traffic





