# coding= utf-8

# is是根据id来判断的, 即指向同一段空间，id表示存储变量值（不是变量名）的那一段内存地址
# id是返回对象的内存地址，变量值是对象，变量名是对对象的引用
# is是内存地址的比较，不是值的比较

# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，
# 而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
a = 1234888888888888888888888888888888888888888000000000000000000000000000000
b = a
print a is b
# 返回结果是True

# 下面是一种比较特殊的情况，但是本质是一样的，主要是python内存管理机制
a = 1234888888888888888888888888888888888888888000000000000000000000000000000
b = 1234888888888888888888888888888888888888888000000000000000000000000000000
# 因为字符较短且靠近，所以Python会将a 和b 变量都指向同一段存储空间
print a is b
print id(a)
print id(b)
# 返回结果True

# 字符串 和整形都是static，不可修改的。

a = "hello my lover"
e = "hello my lover"
print a is e
# 结果还是True

a = 288888.0
b = 288888.0
print a is b
# 结果还是True

# list 等可变量，
>>> a = [1,2,3]
>>> b = [1,2,3]
>>> a is b
False
>>>

