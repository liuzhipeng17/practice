# -*- coding: utf-8 -*-

# 使用dir()可以查看对象的所有属性和方法---查看的是对象，不是类

print(dir('ABC'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
# '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split',
# '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith',
#  'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower',
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，
# 比如__len__()方法返回长度。在Python中，
# 如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()存储过程-动态执行sql-防止sql注入，所以，下面的代码是等价的：


