#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/10/29 上午11:32

def rec(num):
    print(num)
    if int(num/2) > 0:
        return rec(int(num/2))
    print("end", num)

rec(10)

def add(x, y, z):
    return z(x) + z(y)

result = add(-1, -2, abs)
print(result)