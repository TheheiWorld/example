#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/6 上午11:03

import time

# 装饰器本质是个函数
def timer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("the funct run time is %s" % (end_time - start_time))
    return warpper

@timer
def f1():
    time.sleep(3)
    print("in the f1")

f1()