#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W

import gevent
from gevent.server import StreamServer
import os,time
from server.net import hosts
from  server.utils import xpickle

import udp_client

class RequestHandler(object):

    closed = False

    def __init__(self, sock, address):
        self.sock = sock
        self.address = address

        self.f = self.sock.makefile('r')
        self.handle()


    def handle(self):
        while not self.closed:
            t = gevent.spawn(self.read_message)

            t.join()

    def read_message(self):

        message = self.f.readline().strip()
        print message

     
        if not message:
            self.closed = True
            print 'client closed'
            return

ret = os.fork()
if (ret == 0):
    while True:
        if (hosts.get_status()=="on"):
            conf = hosts.get_host_ip()
            for k,v in conf.items():
                res=udp_client.send(k,v)
                print res

        time.sleep(10)



else:


    server = StreamServer(('127.0.0.1', 7777), RequestHandler)
    server.serve_forever()

