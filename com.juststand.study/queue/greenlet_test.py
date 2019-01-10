#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/10 下午2:34

from greenlet import greenlet

def test1():
    print('12')
    g2.switch()
    print('34')
    g2.switch()

def test2():
    print('56')
    g1.switch()
    print('78')

g1 = greenlet(test1)
g2 = greenlet(test2)
g1.switch()