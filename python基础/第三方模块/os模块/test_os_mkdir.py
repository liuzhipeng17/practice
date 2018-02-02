# -*- coding: utf-8 -*-

import os
try:
    os.mkdir("lzp", 0o777) # mode在windows应该是被抛弃的
except FileExistsError as e:
    print(e)

# 文件已经存在会抛出，FileExistsError异常