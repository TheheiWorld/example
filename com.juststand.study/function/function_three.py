#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/9 下午4:06
import functools
r = functools.reduce(lambda x,y:x + y, range(10))
print(r)

f = filter(lambda n:n<5, range(10))
for i in f:
    print(i)

m = map(lambda n:n*n, range(10))
for i in m:
    print(i)
