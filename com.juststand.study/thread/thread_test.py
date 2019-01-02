#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/2 下午6:34

import threading, time

def run(n):
    print("task", n)
    time.sleep(2)

t1 = threading.Thread(target=run, args=('t1', ))
t2 = threading.Thread(target=run, args=('t2', ))
t1.start()
t2.start()