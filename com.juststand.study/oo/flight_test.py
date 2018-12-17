#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/17 下午4:43

class Flight(object):
    def __init__(self, name):
        self.name = name

    def check_status(self):
        print("check status ~~~~")
        return 1

    @property
    def flight_status(self):
        status = self.check_status()
        if status == 1:
            print("success")
        elif status ==0:
            print("failure")
        else:
            print("undefined")

    @flight_status.setter
    def flight_status(self, status):
        print("update", status)

    def __call__(self, *args, **kwargs):
        print("call")

    def __str__(self):
        return self.name

flight = Flight("CA1022")
flight.flight_status
flight.flight_status = "2"
flight()
print(flight.__dict__)
print(flight)
print(type(Flight))