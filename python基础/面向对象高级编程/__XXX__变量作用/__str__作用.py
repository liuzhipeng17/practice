# -*- coding: utf-8 -*-
# __str__定义在类内部，返回类型必须是字符串，在print(这个类实例化对象）时会触发执行


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '<Date object (year:%s, month:%s, day:%s)>' % (self.year, self.month, self.day)


d = Date(2017, 5,12)
# 当没有重写__str__函数的时候，print d 的结果为：
# <__main__.Date object at 0x032280B0>
print(d)

# 当重写__str__后
# Date object <year:2017, month:5, day:12>