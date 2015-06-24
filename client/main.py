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
        except:
            print ("server connect faild")


    def close(self):
        self.client.close()


ci = TcpClient(config.Server,config.Port)

while True:
    Qmsg = server_target.get_data()
    if Qmsg:
        try:
            host_info = Qmsg.get(timeout=1)
            print host_info
            info=xpickle.dumps(host_info)

            ci.send(info)


        except :
            print ("empty")


    sleep(1)










