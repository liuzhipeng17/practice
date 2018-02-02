# -*- coding: utf-8 -*-

# 学习1
import spam

import sys
# sys.modules可以查看内存里面已经加载了哪些模块
print sys.modules['spam']

# 可以访问名称空间spam下的money
print spam.money
# 输出结果为：
# from spam.py
# <module 'spam' from 'F:\oldboy\ģ��\spam.pyc'>
# 0





