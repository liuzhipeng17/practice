# -*- coding: utf-8 -*-

import sys
print sys.path
print sys

# 得到的结果是
# ['F:\\oldboy\\\xc4\xa3\xbf\xe9', 'F:\\oldboy
# <module 'sys' (built-in)>
# 而不是：自己定义的sys.py模块的内容,自定义sys.py内容如下：
    # # -*- coding: utf-8 -*-
    # sys.py
    # print "from my sys.py"
    #
    # path = "from my sys.path"
