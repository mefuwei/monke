#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:f.w
from server.services import linux
class BaseTemplate:
    def __init__(self):
        self.name = None
        self.hostname = None
        self.address = None
        self.os = None
        self.port = None



class LinuxTemplate(BaseTemplate):
    """
    collect the server info including cpu ,mem,load,traffic,hard
    """
    def __init__(self):
        self.name = "linux general template"
        self.services = {
            "cpu":linux.Cpu(),
            "memory":linux.Memory(),
            "load":linux.Load(),
            "traffic":linux.Traffic(),
            "hard":linux.Hard()

        }



class HardTemplate(BaseTemplate):
    """
    collect hard info
    """
    def __init__(self):
        self.name = "hard general template"
        self.service = {

            "hard":linux.Hard()

        }
