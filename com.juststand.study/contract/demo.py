#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/3/14 下午2:03
import time
import hashlib
import base64

get_now_milli_time = lambda : int(time.time() * 1000)

appid = '70b0229f855f9feb46370618e715c6d6'
signKey = 'd108f9b95dd7ce174d50ac8a55fb8fd8'
timestamp = get_now_milli_time()

signStr = signKey + str(timestamp)

def to_md5_value(value):
    md5 = hashlib.md5()
    md5.update(value.encode('utf-8'))
    return md5.hexdigest()

def to_base54_value(value):
    return str(base64.b64encode(value.encode('utf-8')), 'utf-8')


def get_sgin_str(value):
    md5_value = to_md5_value(signStr)
    return to_base54_value(md5_value)

signStr = get_sgin_str(signStr)
print(signStr)

