#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/3/28 下午12:12

import random

origin = []

def add(origin):
    for i in range(7):
        num = random.randint(1, 15)
        origin.append(num)

def sort(origin):
    for index, num in enumerate(origin):
        if index == 0:
            continue
        temp = num
        i = index - 1
        while i >= 0:
            if origin[i] > temp:
                origin[i + 1] = origin[i]
            else:
                break
            i = i - 1
        origin[i + 1] = temp
    print(origin)

add(origin)
sort(origin)

