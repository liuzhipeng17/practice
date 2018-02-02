# -*- coding: utf-8 -*-

# os.stat_result是一个类（也可以说是结构体，因为他没有方法，只有属性）

# os.stat()返回的就是一个os.stat_result对象，还有os.scandir 迭代器里面的元素entry.stat()返回
#也是os.stat_result对象

import os

path = os.path.dirname(os.path.abspath(__file__))
it = os.scandir(path) # it是一个迭代器，在3.6版本支持with上下文管理
for entry in it:
    stat_info = entry.stat() # 包含了文件大小的信息
    print(stat_info.st_size, stat_info.st_mode)

# os.stat_result对象有以下几个成员：
