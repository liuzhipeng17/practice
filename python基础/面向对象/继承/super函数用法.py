# -*- coding: utf-8 -*-

# 需求：子类调用父类的init方法
# 在子类的__init__调用父类的__init__，这种简单的情况当然是可以的，但是许多情况下会出现问题
# 应该采用super()，super可以调用父类的任意函数，不仅仅__init__

# 使用super()的形式：super(当前所在类名字，self对象）.父类函数(该函数的参数，不要self)

# super(TimesFiveCorrect, self).__init__(value)


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Should be 5 * (5 + 2) = 35, and foo.value is %s' % foo.value)
# 这是和mro有关（函数解析顺序，method resolution order)
print(GoodWay.mro())
# 这种菱形继承顺序，是为了避免最顶的超类MyBaseClass继承了两次，
# 所以继承顺序是GoodWay-->TimesFiveCorrect-->PlusTwoCorrect-->MyBaseClass-->object
# 层层调用，先算MyBaseClass,再算PlusTwoCorrect,其次TimesFiveCorrect,最后GoodWay
# 总结，可以归纳如下：
# def GoodWay_init(value):
    # return TimesFiveCorrect_init(value)

# def TimesFiveCorrect_init(value):
    # return PlusTwoCorrect_init(value)

# def PlusTwoCorrect_init(value):
    # return MyBaseClass_init(value)

# def MyBaseClass_init(value):
    # return value

