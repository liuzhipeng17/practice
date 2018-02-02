# -*- coding: utf-8 -*-

# 继承的好处：
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('%s is walking' % self.name)

    def say(self):
        print('%s is saying' % self.name)


class People(Animal):
    pass


class Pig(Animal):
    pass


class Dog(Animal):
    pass


p1 = People('obama', 50)
print(p1.name)
print(p1.age)
p1.walk()

# 继承的作用： 代码的重用性（复用性）

# 派生：在子类定义新的属性： 1 父类没有；2：和父类同名的属性