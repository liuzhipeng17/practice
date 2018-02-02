# -*- coding: utf-8 -*-

# from spam import *
# 如果spam.py里面没有定义__all__列表，那么可以访问spam.py模块所有的变量

# 但是如果spam.py里面有定义__all__列表，那么只能访问__all__列表定义的名字
# note1 __all__列表元素是字符串

from spam_8 import *

print money
print read
# NameError: name 'write' is not defined
# print write