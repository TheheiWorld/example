#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/4 下午2:40

import threading
import time

envent = threading.Event()

def lighter():
    envent.set()
    count = 0
    while True:
        if count >= 5 and count < 10:
            envent.clear()
            print("change to \033[41;1m red \033[0m")
        elif count >= 10:
            envent.set()
            count = 0
            print("change to \033[42;1m green \033[0m")
        else:
            print("change to \033[42;1m green \033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if envent.is_set():
            print("\033[42;1m %s green runing ~~~~ \033[0m" % name)
            time.sleep(1)
        else:
            print("\033[41;1m %s red waiting ~~~~~ \033[0m" % name)
            envent.wait()

l1 = threading.Thread(target=lighter, )
l1.start()

car1 = threading.Thread(target=car, args=('car1', ))
car1.start()