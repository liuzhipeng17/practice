# -*- coding: utf-8 -*-


money = 1
print "before from spam import money, money = %s" % money
from spam import money
import sys
# sys.modules可以查看内存里面已经加载了哪些模块
print sys.modules['spam']

print "after from spam import money, money = %s" % money
# 访问不了名称空间spam下的money
# NameError: name 'spam' is not defined
# print spam.money
# print spam.read

# 输出结果为：
# from spam.py
# <module 'spam' from 'F:\oldboy\ģ��\spam.pyc'>





