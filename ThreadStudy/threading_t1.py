# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/4
@Author      : jim
@File        : threading_t1
@Description : 
"""

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程', self.threadID)
        printTime(self.name, self.threadID, self.counter)
        print('线程结束 ：{}'.format(self.name))


def printTime(threadName, delay, counter):
    while counter:
        print('Thread is:{}, time is:{}'.format(threadName, time.ctime(time.time())))
        time.sleep(delay)
        counter -= 1

thread1 = MyThread(1, 'thread1', 5)
thread2 = MyThread(2, 'thread2', 5)

try:
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('main thread end')
except:
    print('start thread error')


