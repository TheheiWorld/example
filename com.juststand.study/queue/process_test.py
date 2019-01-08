#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/8 下午5:59

import multiprocessing
import time

def run(name):
    time.sleep(1)
    print("hello", name)

if __name__ == '__main__':
    for i in range(10):
        p1 = multiprocessing.Process(target=run, args=('world', ))
        p1.start()
        print(p1.pid)