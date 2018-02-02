# -*- coding: utf-8 -*-


s = 10

def foo():
    print(s)
    s = 12
    print(s)

foo()

# 报错如下：（第七句print(s)出错： 在局部空间foo找到s,但是此时s并没赋值，所以报错
# UnboundLocalError: local variable 's' referenced before assignment
# 词法分析： 只关心三方面：函数声明，形参，局部变量声明；并不会执行
# 在foo函数进行词法分析，只关心一句s = 12（属于局部变量说明）; 相当于声明了一个局部变量s，但并不赋值；
# 赋值是在调用foo（）才会执行

