#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/14 下午10:33

class Animal(object):

    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Dog(Animal):

    def talk(self):
        print("wangwang")


class Cat(Animal):

    def talk(self):
        print('miaomiao')

dog = Dog("dog")
cat = Cat("cat")

Animal.animal_talk(dog)
Animal.animal_talk(cat)