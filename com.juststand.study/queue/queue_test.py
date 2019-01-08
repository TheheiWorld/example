#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/7 下午6:02

import queue
import threading
import time

q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("%s product %s" % (name, count))
        print("%s product %s" % (name, count))
        count += 1

def consumer(name):
    while True:
        if q.qsize() > 0:
            print("%s eat %s" % (name, q.get()))
            time.sleep(1)

t1 = threading.Thread(target= Producer, args=('zhangsan',))
t2 = threading.Thread(target= consumer, args=('lisi',))
t3 = threading.Thread(target= consumer, args=('wangwu',))

t1.start()
t2.start()
t3.start()