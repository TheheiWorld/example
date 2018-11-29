#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/28 下午2:38

import random

checkcode = ''

for i in range(4):
    current = random.randint(0, 3)
    if i == current:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0, 9)
    checkcode += str(temp)

print(checkcode)