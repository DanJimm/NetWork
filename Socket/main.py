# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/6
@Author      : jim
@File        : main
@Description : 
"""

# import socket_t1
import ChatServer
import time
import threading


ChatServer = ChatServer.ChatServer()
ChatServer.start()

while True:
    inter = input('please enter instruct check threadings or enter exit or quit to shutdown server \n >>>')
    if inter.strip() == ('exit' or 'quit'):
        print('server os stoping')
        ChatServer.stop()
        time.sleep(3)
        break
    else:
        print(threading.enumerate())