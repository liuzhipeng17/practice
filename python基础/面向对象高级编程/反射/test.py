# -*- coding: utf-8 -*-

# 在当前模块，找到当前模块对象的内存地址

import sys

x = 11
class FOO:
    pass

def s1():
    print("s1()")

# 拿到当前模块对象
this_module = sys.modules[__name__]
print(this_module)
print(hasattr(this_module, 's1'))
print(getattr(this_module, 's1'))
print(this_module.s1)
print(hasattr(this_module, 'x'))