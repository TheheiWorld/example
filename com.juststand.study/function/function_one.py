#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/10/26 下午3:22

def f1():
    print("function one")

def f2():
    print("function two")
    return 0

def f3():
    print("function three")
    return 1, "hello world", [1, 2, 3], {"name" : "juststand"}

def f4():
    return f3

one = f1()
two = f2()
three = f3()
four = f4()

print(one)
print(two)
print(three)
print(four)
