#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/28 下午4:26

import shutil

f1 = open('hello','r', encoding='utf-8')
f2 = open('world', 'w', encoding='utf-8')

# copy后没有flush
shutil.copyfileobj(f1,f2)

f1.close()
f2.close()

# 这个好
shutil.copytree("./", "module_tree")