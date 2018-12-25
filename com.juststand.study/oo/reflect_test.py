#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/18 下午4:03

class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)

d = Dog("dog")
choice = input(">>>").strip()

if hasattr(d, choice):
    getattr(d, choice)()