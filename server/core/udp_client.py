#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W

import socket

PORT =7600
def send(HOST,data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect((HOST,PORT))

        sock.sendto(data,(HOST, PORT))
        received = sock.recv(1024)
        sock.close()
        if received == "ok":

            res = (HOST,received)

        return res

    except socket.error as reason:

        print("%s %s") % (HOST,reason[1])
        res =(HOST,"failed")
        return res










