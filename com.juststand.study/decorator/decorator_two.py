#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/8 上午10:37

name, pwd = "abc", "abc"

def auth(func):
    def wrapper(*args, **kwargs):
        username = input("username:").strip()
        password = input("password:").strip()

        if username == name and password == pwd :
            print("success")
            func(*args, **kwargs)
        else:
            exit("failure")
    return wrapper

def index():
    print("welcome to index page")

@auth
def home():
    print("welcome to home page")

@auth
def bbs():
    print("welcome to bbs page")

index()
home()
bbs()