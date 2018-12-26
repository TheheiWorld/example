#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/26 上午11:44
'''
1 读取文件名
2 检查文件是否存在
3 打开文件
4 检测文件大小
5 发送文件大小给客户端
6 等客户端确认
7 开始边读边发数据
'''
import socket, os, hashlib

server = socket.socket()
server.bind(("localhost", 6969))
server.listen()
while True:
    conn, addr = server.accept()
    print("new conn", addr)
    while True:
        print("waiting some cmd")
        data = conn.recv(1024)
        if not data:
            print("client is missing ")
            break
        cmd, filename = data.decode().split()
        print(filename)

        if os.path.isfile(filename):
            m = hashlib.md5()
            f = open(filename, 'rb')
            size = os.stat(filename).st_size
            conn.send(str(size).encode())
            # waiting for ack
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("md5=", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())

