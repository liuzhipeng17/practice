# -*- coding: utf-8 -*-

"""
os.scandir得到目录下的子目录（不会递归）和文件信息，返回的是一个迭代器
os.scandir比os.listdir更高效，而且还可以提供文件或目录的属性信息(os.stat)
迭代器的元素是一个os.DirEntry类对象，os.DirEntry常用的方法有：
name(属性）： basename,是一个相对路径的名字
path(属性）：全路径，等效于os.path.join(path, entry.name),如果path是相对路径，entry.path也是相对路径
is_dir(*, follow_symlinks=True): 检查是否是目录，或者指向目录的链接；如果follow_syslinks=False,不会检查链接
is_file()
is_symlink()
stat()

"""

import os

path = os.path.dirname(os.path.abspath(__file__))
# path ='.'
it = os.scandir(path) # it是一个迭代器，在3.6版本支持with上下文管理
for entry in it:
    # print(type(entry)) # entry是一个os.DirEntry类对象，
    print(entry.name,entry.path,entry.is_dir())
    print(entry.stat()) # 包含了文件大小的信息


