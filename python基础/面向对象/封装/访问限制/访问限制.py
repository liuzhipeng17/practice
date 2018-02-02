# -*- coding: utf-8 -*-


class A(object):
    def __init__(self):
        self.__x = 1

    def get_x(self):
        return self.__x

a = A()
# a.__x访问不到
# print a.__x
# 可以访问
print(a._A__x)
# 查看dict
print(a.__dict__)
# {'_A__x': 1}

print(a.get_x())



