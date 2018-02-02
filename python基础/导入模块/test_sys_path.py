# -*- coding: utf-8 -*-

# 跨目录导入模块
#     ss/dir1/spam.py
#     ss/dir2/test_导入包干的那些事.py
#     从test.py要导入spam.py，只能从sys.path做修改（唯一方法，前提test不是包，dir1,dir2不是包）