#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/13 下午3:03

import json, pickle

def hello():
    pass

data = {
    "name" : "juststand",
    "age" : 26
}

file = open("test.txt", "w")
print(json.dumps(data))
file.write(json.dumps(data))
file.close()

f = open("test.txt", "r")
print(json.loads(f.read()))
f.close()