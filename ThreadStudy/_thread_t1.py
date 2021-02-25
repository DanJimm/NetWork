# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/4
@Author      : jim
@File        : _thread
@Description : 
"""

import _thread
import time

#线程执行函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print('thread is:{} time:{}'.format(threadName, time.ctime(time.time())))
        count += 1

def timePrint():
    print('now print time')
    try:
        _thread.start_new_thread(print_time, ('Thread_1', 1))
        _thread.start_new_thread(print_time, ('Thread_2', 2))
    except:
        print('there is a error {}')

    while True:
        pass

