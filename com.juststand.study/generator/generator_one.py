#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/8 下午4:01

g = (i * 2 for i in range(10))

try:
    while True:
        num = g.__next__()
        print(num)
except:
    pass

# 斐波那契数列
def fibonacci(end):
    n, a, b = 0, 0, 1
    while n < end:
        yield b
        a ,b = b, a + b
        n = n + 1
    return "end"

num = fibonacci(10)
print(num)

for i in num:
    print(i)
