#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/19 下午5:55

import socket

server = socket.socket()
server.bind(("localhost", 6969))
server.listen()
conn, addr = server.accept()
print(conn)
print(addr)

data = conn.recv(1024)
print(data)

conn.send(data.upper())
server.close()