#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/3 下午6:06

import threading
import time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread : %s" % n)
    semaphore.release()

if __name__ == "__main__":

    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("ending")
