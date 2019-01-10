#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/10 下午3:04

import gevent

def foo():
    print('running in foo')
    gevent.sleep(1)
    print('running in foo again')

def bar():
    print('running in bar')
    gevent.sleep(2)
    print('switch to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
