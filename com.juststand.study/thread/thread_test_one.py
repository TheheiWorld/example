#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/3 上午11:12

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("runing task:", self.n)
        time.sleep(2)
        print("%s done" % self.n)


t1 = MyThread(1)
t1.setDaemon(True)
t2 = MyThread(2)
t1.start()
# t1.join()
t2.start()