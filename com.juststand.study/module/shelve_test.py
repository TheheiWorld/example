#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/29 上午10:55

'''
linux 上面shelve生成一个 不可读的二进制文件
'''
import shelve, datetime

f = shelve.open('shelve_test.db')
print(f.get('name'))

# info = {'age':20, 'job':'worker'}
# name = ['one', 'two']
#
# f['name'] = name
# f.sync()
# f['info'] = info
# f['date'] = datetime.datetime.now()

f.close()