#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W

import sys
import json
from socket import *
from time import sleep
from conf import config,setting
from core import server_target
from utils import xtime
class TcpClient():

    def __init__(self,SERVER,PORT):

        self.address = (SERVER,PORT)
        self.client = socket(AF_INET,SOCK_STREAM)
        self.client.connect(self.address)

    def send(self,data):
        try:
            self.client.send(data)
            return 0
        except Exception,e:
            print("%s %s") % ("send data failed",e[1])
            self.client.close()
            return 1

    def close(self):
        self.client.close()

try:
    ci = TcpClient(config.Server,config.Port)
except:
    print ("Connect to the remote server failed")
    sys.exit()


while True:
    Qmsg = server_target.get_data()
    if Qmsg:

        host_info = Qmsg.get(timeout=1)

        info=json.dumps(host_info)

        result = ci.send(info+"\r\n")

        if result ==1:
            #重连服务器
            while True:
                try:
                    ci = TcpClient(config.Server,config.Port)
                    print ("%s reconnect success") % xtime.strdatetimefromats(xtime.timestamp())
                    break
                except Exception,e:
                    print("%s %s %s") % (xtime.strdatetimefromats(xtime.timestamp()),config.Server,e[1])
                sleep(5)
        sleep(1)










