# -*- coding:utf-8 -*-



class Foo(object):
    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__

obj['k2'] = 'wupeiqi'  # 自动触发执行 __setitem__

del obj['k1']  # 自动触发执行 __delitem__