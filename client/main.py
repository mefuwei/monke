#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
from client.utils import xpickle
from client.core import server_target
from socket import *

from time import sleep

from client.conf import config

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
            print ("server connect failed",e)
            return 1



    def close(self):
        self.client.close()


ci = TcpClient(config.Server,config.Port)
import json

while True:


    Qmsg = server_target.get_data()
    if Qmsg:
        try:
            host_info = Qmsg.get(timeout=1)

            info=json.dumps(host_info)

            result = ci.send(info+"\r\n")

            if result ==1:
                #重连服务器
                ci = TcpClient(config.Server,config.Port)

        except Exception,e:

            print ("empty",e)


        sleep(1)










