#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/10 下午4:42

import socket
import gevent
from gevent import monkey

monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(('localhost', port))
    s.listen(500)

    while True:
        cli, addr = s.accept()
        gevent.spawn(handle, cli)

def handle(conn):
    try:
        while True:
            data = conn.recv(1024)
            print('data:', data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    server(8888)