# -*- coding: utf-8 -*-

import sys
# import模块，会从sys.path搜索(内置模块除外，内置模块不是.py文件）
print sys.argv
# 是一个列表
# argv[0] 是py文件名（没有.py)
# 剩余的是后面的参数
username = sys.argv[1]
password = sys.argv[2]