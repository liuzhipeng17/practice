# coding= utf-8


class Student(object):
    country = 'China'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def study(self):
        print("study")

s = Student('lzp', 'male')

