# -*- coding: utf-8 -*-


class A(object):
    def fa(self):
        print('from a')

    def test(self):
        self.fa()


class B(A):
    def fa(self):
        print('from b')

b = B()
b.test()
# 结果为from b，记住mro
# b.test寻找顺序: b-->B-->A找到了test, 执行b.fa
# b.fa寻找顺序： b-->B找到，执行print 'from b'
