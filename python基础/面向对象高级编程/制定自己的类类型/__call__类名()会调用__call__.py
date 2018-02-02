# -*- coding: utf-8 -*-


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('exec __call__')


f = Foo('lap')
f()# 对象()会再类定义里面查找__call__
print(callable(f))