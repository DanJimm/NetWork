# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/6
@Author      : jim
@File        : ChatServer
@Description : 
"""

import socket
import threading
import logging
import time

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ChatServer:
    def __init__(self, laddr = ('127.0.0.1', 9999)):
        self.server = socket.socket()
        self.laddr = laddr
        self.clients = {}

    def start(self):
        try:
            self.server.bind(self.laddr)
            self.server.listen()
            print('server started')
        except:
            print('server stared error')
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while True:
            try:
                c, raddr = self.server.accept()
                logger.info('there is a client login:>>>' + str(c))
                threading.Thread(target=self.recv, name='recv', args=(c, raddr)).start()
                for c in self.clients.values():
                    c.send('{} is logging!'.format(c.getpeername()))
                self.clients[raddr] = c
            except:
                logging.info('server end')
                break

    def recv(self, client:socket.socket, raddr):
        while True:
            try:
                message = client.recv(1024)
                logger.info(message)
                send_Message = 'from client {} ,time {} recv message:{}'.format(\
                    client.getpeername(),\
                    time.ctime(time.time()),
                    message.decode()).encode()
                # client.send('ack {}'.format((message.decode())).encode())
                for c in self.clients.values():
                    c.send(send_Message)
            except:
                logger.info('client down line {}'.format(client.getpeername()))
                del self.clients[raddr]
                exit_Message = 'from client {} ,time {} exit'.format( \
                    client.getpeername(), \
                    time.ctime(time.time())).encode()
                for c in self.clients.values():
                    c.send(exit_Message)
                client.close()
                break

    def stop(self):
        for i in self.clients.values():
            print('i is',i)
            i.close()
        time.sleep(3)
        self.server.close()


