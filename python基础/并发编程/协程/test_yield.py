# -*- coding: utf-8 -*-


def f():
    print("start")
    current = yield
    while True:
        value = yield current
        current = value + 5


g = f()
next(g) # print start 然后停止在第5行
print(g.send(10))
print(g.send(20))
# 生成器在收到send函数之后，会将send函数的值视为yield 右侧表达式的结果，
# 而且评估完当前的yield 表达式后，程序会继续推进到下一个yield表达式那里，
# 此时会将yield 右侧表达式的结果当成send()函数的返回值，返回给外界。

# g.send(10)的代码可视为：
# def f():
#     current = 3
#     while True:
#         return current
# 接着的g.send(20)的代码可视为：实在while True里面开始的
# value = 20
# current = value + 5
# while True:
#     return current


def f2():
    print("start f2")
    current = yield
    while True:
        value = yield current
        current = value + 5

# 如果有两个current = yield表达式呢？
#
g = f2()
next(g) # 打印
g.send(3) # 碰到current = yield， 将yield 表达式结果为3,并将其赋值为current = 3,
# 然后执行while True, 碰到第二个value = yield current ,此时current = 3,所以send(3)的返回值为3
