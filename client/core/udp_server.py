#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W

import SocketServer
from core import config_handle



class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):

        data = self.request[0].strip()
        socket = self.request[1]
        server_addr = self.client_address[0]

        config_handle.save_conf(data)


        socket.sendto("ok", self.client_address)

def udp_server():
    HOST, PORT = "0.0.0.0", 7600

    server = SocketServer.UDPServer((HOST, PORT),MyUDPHandler)

    server.serve_forever()