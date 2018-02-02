# -*- coding: utf-8 -*-

"""
通过自顶向下或自底向上遍历树，在目录树中生成文件名。
对于位于目录顶部(包括顶部本身)的树中的每个目录，
它会产生一个3元组(dirpath、dirnames、filenames)。

dirpath 是一个字符串， dirnames是 dirpath下的子目录列表， filenames是dirpath下的文件列表
filename是不包含目录的文件名，所以要想得到filename的路径：os.path.join(dirpath,filenames[0])
"""
# import os
# from os.path import join, getsize
#
# # 同级所有目录下文件的大小，排除名为CVS的目录和子目录
# path = os.path.dirname(os.path.abspath(__file__))
# for root, dirs, files in os.walk(path):
#     print(root, "consumes", end=" ") # 添加了 end = "" 表示不换行，并且以空格隔开两条print语句
#     print(sum(getsize(join(root, name)) for name in files), end=" ")
#     print("bytes in", len(files), "non-directory files")
#     if 'CVS' in dirs:  # 这里并不是删除CVS目录，只是将CVS目录排除在外
#         dirs.remove('CVS')  # don't visit CVS directories


# 下面是一个删除目录的实现,（将整个目录删除）
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os

top =os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
for root, dirs, files in os.walk(top, topdown=False): # 主要是将topdown = False，自底向上删
    for name in files:
        os.remove(os.path.join(root, name)) # 现将文件删除了，目录变成空目录，
    for name in dirs:
        os.rmdir(os.path.join(root, name)) # 目录变成空目录，可以删了

os.rmdir(top)