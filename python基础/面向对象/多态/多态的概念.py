# -*- coding: utf-8 -*-

# 使得继承体系中的多个类都能以各自所独有的方式实现某个方法
# 多态是继承的另一个好处，继承还有代码重用的好处
# 有了继承，才能有多态。

# 要理解多态，首先要理解数据类型，当我们定义了一个class,实际上定义了一种类型
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
# 多态性： 定义统一接口，可以传入不同类型的数据，


class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'

# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
a = Animal()
c = Cat()
d = Dog()

print isinstance(a, Animal)
print isinstance(c, Animal)
print isinstance(a, Cat)
# 要理解多态性，还需要定义一个函数，这个函数接受一个Animal类型的变量


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(a)
run_twice(c)

# 你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
# 由于Animal类型有run()存储过程-动态执行sql-防止sql注入，因此，传入的任意类型，只要是Animal类或者子类，
# 就会自动调用实际类型的run()存储过程-动态执行sql-防止sql注入，

# 这就是多态的意思：
    # 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
    # 就可以放心地调用run()存储过程-动态执行sql-防止sql注入，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
    # 由运行时该对象的确切类型决定，

# 这就是多态真正的威力：
    #      调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
    #      只要确保run()方法编写正确，不用管原来的代码是如何调用的。


# 这就是著名的“开闭”原则：
    # 对扩展开放：允许新增Animal子类；
    # 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。