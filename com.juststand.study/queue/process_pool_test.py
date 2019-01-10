#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/9 下午5:43

from multiprocessing import Process, Pool
import time
import os

def Foo(i):
    time.sleep(1)
    print('%s doing' % os.getpid())
    return i + 100

def Bar(arg):
    print('--> exec done:', arg)

pool = Pool(5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)
    # pool.apply(func=Foo, args=(i, ))

pool.close()
pool.join()
print("end")
