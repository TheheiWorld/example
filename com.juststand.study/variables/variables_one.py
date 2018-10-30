#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/10/29 上午11:14

# 不好的方式
def change_name():
    global name
    name = "maitao"

change_name()
print(name)