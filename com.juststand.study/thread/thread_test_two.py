#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/3 下午3:58

import threading
import time

def run(n):
    lock.acquire()
    global num
    time.sleep(1)
    num += 1
    lock.release()

lock = threading.Lock()
num = 0

t_obj = []
for i in range(100):
    t = threading.Thread(target=run, args=('%s-task' % i,))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print("the task is ending :", threading.current_thread())
print("num = ", num)
