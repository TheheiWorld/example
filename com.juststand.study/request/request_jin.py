#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/12/30 下午4:06

import requests
import threading

def create_users(payload):
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    r = requests.post("https://cecservice.12301.cn/12301/third/sendverif", headers=headers,params=payload)
    print(r.json())

def thread_request():
    payload = {
        'mobile' : '18855158810',
        'contractId' : 'EIN9NSQBSOW1'
    }
    create_users(payload)

def create_thread():
    threads = []
    for i in range(0, 20):
        t = threading.Thread(target=thread_request, args=)
        threads.append(t)
    return threads

if __name__ == '__main__':
    threads = create_thread()
    for thread in threads:
        thread.start()


