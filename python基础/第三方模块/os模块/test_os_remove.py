# -*- coding: utf-8 -*-

# remove 用来删除文件，如果是目录，会抛出osError异常。
# 删除目录，用rmdir()，
# remove(path)中的path支持相对路径

import os

os.remove("lzp.txt") # 支持相对路径