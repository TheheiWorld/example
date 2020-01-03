#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/3/27 下午3:59

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
from tornado.options import define, options
import http.server
import datetime
import os


define("port", default=12345, help="run on given port", type=int)

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hello world")

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()