#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/23 下午4:40

import os, time, datetime
import random

print(__file__)
print(os.path.abspath(__file__))

print(time.time())
print(time.localtime())

current_time = time.localtime()
print(current_time.tm_year)
print(current_time.tm_mon)
print(time.strftime('%Y-%m-%d'))

print(datetime.datetime.now())

print(random.random())
print(random.randrange(1, 3))
