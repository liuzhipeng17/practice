# -*- coding: utf-8 -*-

test_list = [1,2,3] # 全局空间的test_list


def change():
    # 这样相当于在内部定义了名字（内置空间的test_list)
    test_list = [1,6]

print "before change test_list= %s" % test_list  #全局空间的test_list
change()
print "after change test_list= %s" % test_list   #全局空间的test_list
# before change test_list= [1, 2, 3]
# after change test_list= [1, 2, 3]

# 如果不是作为参数传递，test_list不会改变
# 如果作为参数传递，有哪些变化呢？
