
# -*- coding: utf-8 -*-

# 有两种情况：
# 一种情况： =后面跟的另外一段内存地址的话，不会更改
# 另外一种情况：在原来内存地址直接修改append, 会更改

test_list = [1, 2, 3]  # 全局空间的test_list
def change(t):
    # t也是内置空间的名字t
    t = t + [1, 6]

print "before change test_list= %s" % test_list  # 全局空间的test_list
change(test_list)
# t = test_list, t和test_list都是对同一内存地址的引用
# t = t + [1,6] 更改t为对另外一个内存的引用
# 如果改成t += [1,6]，情况又有所不同（会更改的）
print "after change test_list= %s" % test_list  # 全局空间的test_list

