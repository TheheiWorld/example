#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/9 下午3:11

from collections import Iterator
a = [1, 2, 3]
print(isinstance(a, Iterator))
print(isinstance(iter(a), Iterator))