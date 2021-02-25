# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/6
@Author      : jim
@File        : socket_t1
@Description : 
"""

import socket

server = socket.socket()
laddr = ('127.0.0.1', 9999)

server.bind(laddr)
server.listen()

print('im waiting for client')
c, raddr = server.accept()
print('client is {},ip is {}'.format(c, raddr))

while True:
    mes = (c.recv(1024).decode())
    print('resev mes:{}'.format(mes))
    c.send('reseved mes:{}'.format(mes).encode())
    if mes == 'quit' or mes == 'exit':
        print('bye')
        c.send(b'\n bye')
        break
