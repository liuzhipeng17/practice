# -*- coding: utf-8 -*-

"""
和basename相对应的是dirname,获取的split的第一个元素
"""
import os
path = "fool\\bar"
print(os.path.split(path))
print(os.path.basename(path))
print(os.path.dirname(path))
