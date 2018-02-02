# -*- coding: utf-8 -*-

# @classmethod 把一个方法绑定给类, 会把类名自动传递给函数的第一个参数cls
# 对象也可用，


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def test(cls, x):
        print(cls,x)
        # cls是类，类的作用：实例化，属性引用

    def temp(self):
        pass

Date.test(2)
