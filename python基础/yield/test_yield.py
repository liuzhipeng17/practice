# -*- coding: utf-8 -*-


def f():
    print("start")
    current = yield "hello"
    print('current=', current)
    while True:
        value = yield "bad"
        print("value=",value)
        # value = value + 'not' # 此行会报错，因为value会为整形, 不能和字符串进行相加


# g = f()
# s1 = next(g)
# print('s1=',s1)
# 第一次Next时，停止在第5行, 将yield右边的表达式（无即None)作为next()的返回值

# s2 = next(g)
# print('s2=', s2)
# 第二次的next,会将None作为yield表达式" yield hello"的值赋给current, 即current = None
# 然后程序往下执行，遇到yield "bad"停止，将yield右边的表达式"bad"作为第二次next的返回值

# s3 = next(g)
# print('s3=',s3)
# 第三次next,会将None作为yield表达式”yield bad"的值赋给value, 即value = None,
# 程序往下执行，遇到value = yield "bad"停止，将"bad"作为第三次next的返回值

g = f()
s1 = next(g)# 这一步不能少
# 第一次Next时，停止在第5行, 将yield右边的表达式（无即None)作为next()的返回值
print(g.send(10))
# 生成器调用第一次send时，将send参数10代替表达式"yield hello"的值，赋给current,
# 然后程序往下执行，在遇到yield bad停止，将"bad"作为第一次send()函数的返回值返给外界
print(g.send(20))
# 生成器第二次调用send时，将send参数20代替表达式"yield bad"赋给 value
# 程序往下执行，然后遇到yield bad停止，将"bad"作为第二次send()函数的返回值返给外界

# 生成器在收到send函数之后，会将send函数参数的值视为yield表达式（注意不是yield右侧的表达式）的结果，
# 而且评估完当前的yield 表达式后，程序会继续推进到下一个yield那里，
# 此时会将yield 右侧的表达式（注意不是yield表达式）的结果当成send()函数的返回值，返回给外界。



# g.send(10)的代码可视为：接着print("start")
#     current = 10
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
# g = f2()
# next(g) # 打印
# g.send(3) # 碰到current = yield， 将yield 表达式结果为3,并将其赋值为current = 3,
# # 然后执行while True, 碰到第二个value = yield current ,此时current = 3,所以send(3)的返回值为3
