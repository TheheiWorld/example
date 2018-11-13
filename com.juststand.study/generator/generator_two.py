#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/8 下午4:01
import time

def consumer(name):
    print("%s prepare to eat " % name)
    while True:
        b = yield
        print(" b %s is coming, %s eat b" % (b, name))


def producer(name):
    tom = consumer("Tom")
    tony = consumer("Tony")
    tom.__next__()
    tony.__next__()

    for i in range(10):
        print("%s start to work" % name)
        time.sleep(1)
        tom.send("food %s" % i)
        tony.send("food %s" % i)

producer("cooker_ma")
