#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/10/26 下午3:49


def f1(x, y):
    print(x)
    print(y)

# 位置参数
f1(1, 2)
# 关键字参数 不能写在位置参数前
f1(y=2, x=1)
f1(1, y=3)

# 默认参数 非必传
def f2(x, y=2):
    print(x)
    print(y)

f2(1)

# 参数组 不定参数
def f2(*args):
    # args 分装成 tuple
    print(args)

f2(1,2,3,4)

# 键值对 字典
def f3(**kwargs):
    print(kwargs)

f3(name='juststand', age=22)

school = "maitao"

# 不好的方式
def change_name():
    global school
    school = "heima"
    print(school)

change_name()
print(school)