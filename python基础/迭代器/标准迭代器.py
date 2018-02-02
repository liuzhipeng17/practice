# coding=utf-8
# 迭代的定义：给定一个list或tuple，
# 我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）



# 为什么要迭代器：
# 迭代器提供了一种不依靠下标索引方式来遍历可迭代对象，如字典，文件
# 迭代器和列表更省内存，迭代器是惰性计算
# 缺点：
    # 只能往后取值

# 判断一个对象是否可迭代：
from collections import Iterable
print(isinstance('cc', Iterable))

# 遍历list,推荐采用enumerate
for i, value in enumerate([1,2,'3']):
    print("%d -> %s" % (i, value))

# 遍历字典：
dic = {'name': 'lzp', 'sex': 'male'}
for k, v in dic.items():
    print("%s:%s" % (k, v))

# 迭代器遍历字典 python2不行
# iter_test = dic.__iter__()
# while True:
#     try:
#         print iter_test.next
#     except StopIteration:
#         break

# 遍历文件
# with open('a.txt', 'rb') as f:
#     for line in f:
#         print line