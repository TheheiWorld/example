#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/12/14 上午11:46

class School(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, student):
        print("%s is coming" % student.name)
        self.students.append(student)

class SchoolMemeber(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        pass

class Student(SchoolMemeber):

    def __init__(self, name, age, id, grade):
        super(Student, self).__init__(name, age)
        self.id = id
        self.grade = grade

    def tell(self):
        print('''
        name:%s
        age:%s
        id:%s
        grade:%s
        ''' % (self.name, self.age, self.id, self.grade))

    def pay(self, amount):
        print("%s pay %s" % (self.name, amount))


class Teacher(SchoolMemeber):

    def __init__(self, name, age, salary, course):
        super(Teacher, self).__init__(name, age)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        name:%s
        age:%s
        salary:%s
        course:%s
        ''' % (self.name, self.age, self.salary, self.course))

    def teach(self):
        print("%s teaches %s" % (self.name, self.course))

school = School("school1", "shanghai")
teacher = Teacher("teacher1", 33, 90, "chinese")
student = Student("student1", 22, 1, "G1")
school.enroll(student)
print(school.students)
for s in school.students:
    print(s.tell())
