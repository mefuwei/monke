#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
import os
def monitor():
    """
    return a dict including %user, %iowait,%idle
    """
    cmd = "sar -C 1 3|awk 'END {print}'"
    result = (os.popen(cmd).read()).strip()
    if result:
        cpu_list = result.split()
        user,iowait,idle = float(cpu_list[2]),float(cpu_list[5]),float(cpu_list[7])
        values = {
            "user" : user,
            "iowait": iowait,
            "idle":idle
        }

    else:
        values = None
        print """error:
    please check the command 'sar',
    install :yum install sysstat,sudo apt-get install sysstat
        """
    return values


