#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
from genneral import Defaultservice

class Load(Defaultservice):
    def __init__(self):
        self.name = "load"
        self.interval = 300
        self.plugin_name = "load_info"
        self.triggers ={
            "load1" : [5,9],
            "load5" : [5,9],
            "load15" : [5,9],
            'uptime':None

        }
class Cpu(Defaultservice):
    def __init__(self):
        self.name = 'cpu'
        self.interval = 10
        self.plugin_name = "cpu_info"
        self.triggers = {
            "cpu_idle":[20],
            "cpu_iowait":[20]
        }
class Memory(Defaultservice):
    def __init__(self):
        self.name = "memory"
        self.interval = 300
        self.plugin_name = "memory_info"
        self.triggers = {
            'mem_total':[None],
            'mem_used':[90]
        }


class Traffic(Defaultservice):
    def __init__(self):
        self.name = "Traffic"
        self.interval = 120
        self.plugin_name = 'traffic_info'
        self.triggers = {
            "out" :[],
            "into":[]
        }


class Hard(Defaultservice):
    def __init__(self):
        self.name = "hard"
        self.interval = 120
        self.plugin_name = 'hard_info'
        self.triggers = None

