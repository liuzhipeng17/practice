# -*- coding: utf-8 -*-


class Fib(object):
    def __init__(self):
        print('__init__')
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        print('exec __iter__')
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        print('exec next')
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

f = Fib()
for i in f:
    print(i)

# 输出结果如下：
# __init__
# exec __iter__
# exec next
# 1
# exec next
# 1
# exec next
# 2
# exec next
# 3
# exec next
# 5
# exec next
# 8
# exec next
