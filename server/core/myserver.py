#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
from multiprocessing import Process
import gevent
from gevent.server import StreamServer
import os
import time
import json
from server.net import hosts
import udp_client
from server.utils import xtime

class RequestHandler(object):

    closed = False

    def __init__(self, sock, address):
        self.sock = sock
        self.address = address
        self.r = self.sock.recv(1024)
        self.f = self.sock.makefile('r')
        self.handle()


    def handle(self):
        while not self.closed:
            t = gevent.spawn(self.read_message)
            t.join()

    def read_message(self):

        message = self.f.readline().strip()

        if not message:
            self.closed = True
            print 'client closed'
            return

        data = json.loads(message)

        redis_key = "%s::%s" % (data["hostname"],data["service_name"])
        recv_time = xtime.timestamp()

        data["time"] = recv_time
        print data
        #实例化ｒｅｄｉｓ

        redis = hosts.r
        redis.put_pk_data(redis_key,redis_key,data)

#启动一个子进程发送主机配置
def send_monitor_conf():


    while True:

        if (hosts.get_status()=="on"):
            conf = hosts.get_host_ip()
            for k,v in conf.items():
                res=udp_client.send(k,v)
                print(res)
                time.sleep(0.5)
        time.sleep(10)

p = Process(target=send_monitor_conf,args=())
p.start()

#启动收据接收服务
server = StreamServer(('0.0.0.0', 7777), RequestHandler)

server.serve_forever()

