# coding= utf-8

# 需求：子类派生出一个name属性，同时还要保留原来的value属性
# 在子类的__init__调用父类的__init__，这种简单的情况当然是可以的，但是许多情况下会出现问题
# 应该采用super()，后续介绍


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self, name, value):
        MyBaseClass.__init__(self, value)
        self.name = name



#