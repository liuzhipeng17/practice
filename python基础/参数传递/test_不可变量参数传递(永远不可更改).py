# -*- coding: utf-8 -*-

test = 3# 全局空间的test


def change(t):
    # 这样相当于在内部定义了名字（内置空间的test)
    t += 4

print "before change test_list= %s" % test  #全局空间的test_list
change(test)
print "after change test_list= %s" % test   #全局空间的test_list