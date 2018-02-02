# -*- coding: utf-8 -*-

"""os.path.basename是获取文件名（这种说法是片面的）
这个是函数是调用os.path.split(path)[1]
是将路径按路径分隔符分开，而且最后一个
如果Path = "/foo/bar/“，那么os.path.basename()得到的是一个空字符
"""

import os

path = os.path.dirname(os.path.abspath(__file__))
print(os.path.split(path))

print(os.path.basename(path))

path = "fool\\bar\\"
print(os.path.split(path))

