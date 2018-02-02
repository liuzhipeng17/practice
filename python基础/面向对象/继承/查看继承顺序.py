# -*- coding: utf-8 -*-

# 广度优先：F->D->B-E->C->A->object (F继承D,E ; D继承B， B继承A；E继承C，C继承A）
# 查看继承顺序：类名.__mro__


class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print ('from B')

class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from C')


class F(D, E):
    pass
    # def tests(self):
    #     print 'from F'

f1 = F()
print(F.__mro__)

# (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)


