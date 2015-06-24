#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
class Defaultservice():
    def __init__(self):
        self.name ='DefaultService'
        self.interval = 300
        self.plugin_name = None
        self.data_from = "agent"
        self.triggers = {}
        self.graph_index={
            'index':[],
            'title':self.name
        }
