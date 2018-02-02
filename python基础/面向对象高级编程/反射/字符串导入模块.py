# -*- coding: utf-8 -*-

# 字符串导入模块的方式：

# 1
# m = raw_input("please input your model").strip()
#
# m1 = __import__(m)
# print m1

# 2
import importlib
t = importlib.import_module('time')

print(t.time())