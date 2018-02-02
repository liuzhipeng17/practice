# coding=utf8

# 闭包是指：内部函数的代码包含对外部作用域名字的引用，但不是对全局作用域名字的引用
# 闭包是指：是一种定义在某个作用域A的函数，这个函数应用了那个作用域A的变量（这个作用域应该是函数内部）
# Python的函数是一级对象(first-class object)，可以直接引用函数，把函数赋给变量，把函数当做参数传给其他函数，
# 闭包，返回的不仅仅是函数，还有闭包函数引用到的闭包变量

x = 1
def function_1():
    def function_2():
        print(x)
        # funtion_2不是闭包


def function_1(x):
    def function_2():
        print(x)
        # funtion_2是闭包

def function_3():
    x = 2
    def function_4():
        print x
    return function_4
    # funtion_4闭包

f = function_3()
f()
print f.__closure__[0].cell_contents
print f.__closure__
# 为None说明不是闭包
# 为元组形式，元素是闭包函数应用到的变量
