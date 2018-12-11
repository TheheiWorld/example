#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/11 下午5:34

class person:

    default_name = 'zhangsan'
    sport = []

    def __init__(self, name, age, desc):
        self.name = name
        self.age = age
        self.desc = desc

print(person.default_name)

p1 = person('liso', 12, "desc")
p1.sport.append("basketball")
print(p1)
p1.default_name = "wangwu"
print(p1.default_name)

p2 = person('l', 12, "desc")
p2.sport.append('score')
print(p2.default_name)
print(p2.sport)