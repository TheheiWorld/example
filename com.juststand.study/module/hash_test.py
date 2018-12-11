#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/8 下午7:48

import hashlib

m = hashlib.md5()
m.update(b'hellow')
print(m.hexdigest())
