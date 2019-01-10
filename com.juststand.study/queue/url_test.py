#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/1/10 下午3:52

from urllib import request
import gevent, time
from gevent import monkey

# 让gevent感知urllib这种io操作
monkey.patch_all()

def url(url):
    res = request.urlopen(url)
    data = res.read()
    print('size =', len(data))

urls = [
    'https://www.maitao.com',
    'https://www.python.org',
    # 'http://www.theheiworld.top'
]

start = time.time()
gevent.joinall([
    gevent.spawn(url, 'https://www.maitao.com'),
    gevent.spawn(url, 'https://www.python.org'),
    # gevent.spawn(url, 'http://www.theheiworld.top'),
])
end = time.time()
print(end-start)

for u in urls:
    url(u)
end1 = time.time()
print(end1 - end)
