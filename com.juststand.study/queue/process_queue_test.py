#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/9 下午4:35

from multiprocessing import Queue, Process

def f(q):
    q.put([41, 'hello world'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    print(q.get())
