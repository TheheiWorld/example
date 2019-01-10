#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/10 下午4:47

import socket

HOST = 'localhost'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input('>>'), encoding='utf8')
    s.sendall(msg)
    # data = s.recv(1024)
