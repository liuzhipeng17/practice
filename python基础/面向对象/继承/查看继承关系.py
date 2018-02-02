# -*- coding: utf-8 -*-

# 怎么查看类的继承 类名.__bases__


class Student(object):
    country = 'China'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.score = 0

    def view_score(self):
        self.score = 90

s = Student('lzp', 'male')

print(Student.__bases__)
# (<type 'object'>,)
