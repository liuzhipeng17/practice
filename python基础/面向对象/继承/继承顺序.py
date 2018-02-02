# -*- coding: utf-8 -*-

# 继承顺序（查找属性）新式类：广度优先，经典类：深度优先

# 广度优先：F->D->B-E->C->A->object (F继承D,E ; D继承B， B继承A；E继承C，C继承A）--菱形继承
#           F->D->B->X->E->C->Y->object(F继承D,E ; D继承B， B继承X；E继承C，C继承Y)--Y型继承

# 例子F继承D,E ; D继承B， B继承A；E继承C，C继承A


class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


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
f1.test()

