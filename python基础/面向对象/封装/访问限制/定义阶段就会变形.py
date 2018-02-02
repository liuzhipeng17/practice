# -*- coding: utf-8 -*-


class A(object):
    def __fa(self): # 变形_A__fa
        print('from a')

    def test(self):
        self.__fa() # 变形self._A__fa


class B(A):
    def __fa(self):# 变形_B__fa
        print('from b')

b = B()
b.test()
b._A__fa()
# 结果为from a，记住mro
# b.tests()会执行b._A__fa(); 因为在b对象找不到test，在B类找不到，在A找到,执行_A__fa,
# __开头的属性和方法不能被子类覆盖，可以被继承
