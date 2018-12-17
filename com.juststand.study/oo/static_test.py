#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/17 下午3:48

class Dog(object):

    language = "chinese"

    def __init__(self, name):
        self.name = name

    # @staticmethod #本质上和类实例没什么关系
    @property
    def eat(self, food):
        print("%s eats %s" % (self.name, food))

    @eat.setter
    def eat(self):
        pass

    @classmethod # 类方法只能访问类变量，不能访问实例变量
    def talk(self):
        print("%s talk" % self.language)

# 实际代码不存在
dog = Dog('demo')
# Dog.eat(dog, "food")
dog.talk()