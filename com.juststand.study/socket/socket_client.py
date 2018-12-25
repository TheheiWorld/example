#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/19 下午5:47

import socket

client = socket.socket()
client.connect(('localhost', 6969))
client.send(b"hello world")

data = client.recv(1024)
print(data)

client.close()
