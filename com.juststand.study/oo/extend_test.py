#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/14 上午11:21
'''
python3 支持多继承 优先级 广度优先
'''

class A(object):
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B, C):
    # def __init__(self):
    #     print("D")
    pass

d = D()

