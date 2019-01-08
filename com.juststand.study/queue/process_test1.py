#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/8 下午6:18

import multiprocessing
import os

def info(name):
    print(name)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())
    print("\n")

def f(name):
    info("create process")
    print("hello", name)

if __name__ == '__main__':
    info("parent")
    p1 = multiprocessing.Process(target=f, args=('new', ))
    p1.start()
