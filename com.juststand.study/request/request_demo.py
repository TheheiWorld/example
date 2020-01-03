#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/12/30 下午4:06

import requests
import threading

def create_users(payload):
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    r = requests.post("http://192.168.0.84:8004/user/create", headers=headers,params=payload)
    print(r.json())

def thread_request(i):
    payload = {
        'mobile' : '9980000' + str(i),
        'nickname' : 't8_lichongyang' + str(i),
        'sex' : "1",
        'city' : '2',
        'laxinType' : '13',
        'appidType' : '2',
        'brokeruid' : 'U0611607181353431550'
    }
    create_users(payload)

def create_thread():
    threads = []
    for i in range(0, 100):
        t = threading.Thread(target=thread_request, args=(i,))
        threads.append(t)
    return threads

if __name__ == '__main__':
    threads = create_thread()
    for thread in threads:
        thread.start()


