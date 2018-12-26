#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/26 上午11:44

import socket, hashlib

client = socket.socket()
client.connect(('localhost', 6969))

while True:
    cmd = input(">>").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        size = client.recv(1024)
        print("size=", size)

        client.send("start to read file".encode())
        file_size = int(size.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open('new_' + filename, 'wb')

        m = hashlib.md5()
        while received_size < file_size:
            # 防止粘包
            surplus = file_size - received_size
            if surplus > 1024:
                surplus = 1024
            data = client.recv(surplus)
            received_size += len(data)
            f.write(data)
            m.update(data)
            print(data, received_size, file_size)
        else:
            print("receive done")
            f.close()
            new_file_md5 = m.hexdigest()
        sever_md5 = client.recv(1024)
        print(sever_md5, new_file_md5)

        if sever_md5.decode() != new_file_md5:
            print('file error')
