#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W


import os


def collect():
    """
    return a dict including disk_total disk_used mem_total
    """

    command = "cat /proc/meminfo |grep MemTotal|awk -F' ' '{print $2}'"
    memTotal_f = round(float(os.popen(command).read())/1024/1000,0)
    memTotal = int(memTotal_f)
    cmd = 'df -h |grep "/dev/s"'
    metric_disk = os.popen(cmd).readlines()
    hardNum=[]
    for i in metric_disk:
        hard_space = float((i.strip().split()[1])[:-1])
        hardNum.append(hard_space)

    disk_info = sum(hardNum)
    disk_use = {}
    metric_disks=os.popen('df -x tmpfs -x devtmpfs | grep -Eo " /\S*$" ').readlines()
    for disk in metric_disks:
        cmd = 'df|grep -E "%s$"' % disk.strip()
        disks = os.popen(cmd).readlines()[0]
        disk_list = disks.split()
        disk_use[disk_list[5]]=disk_list[4]
    hard = {
        "disk_used" : disk_use,
        "disk_total":disk_info,
        "mem_total":memTotal
    }

    return hard
