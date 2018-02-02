# -*- coding: utf-8 -*-

# @staticmethod 就是一个类方法，不需要实例化就可以调用，调用形式：类名.method， 定义的时候没有self参数;
# 当然也可以用实例化对象调用

import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


d = Date(2017,8,17)
print(d.year, d.month, d.day)
# 可以类对象调用，
d1 = Date.now()
print(d1.year, d1.month, d1.day)
# 可以用实例化对象调用
d2 = d.now()
print(d2.year, d2.month, d2.day)