# -*- coding: utf-8 -*-

# @property装饰器负责把一个类方法(动词)变成属性(名词）
# property 属性优先级高于实例化对象属性 即self.score会优先查找property，没有在查找对象的score


class Student(object):
    def __init__(self, score):
        # self.__score = score # 这种情况，初始化还是可以输入字符串的，
        self.score = score # self.score = score 会调用@score.setter def score(self, score)
        # self.score 会调用@property的def score

    @property
    def score(self):
        return self.__score # 可以看到这里是__score

    @score.setter # 可以控制实例化时，传入参数的类型和范围
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be in 0~100')

        self.__score = value # 是__score，所以最终的是结果是： score最终赋给self.__score

    @score.deleter
    def score(self):
        # del self.__score
        raise Exception("score is permitted delete")


p = Student(99)
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
print(p.score)
p.score = 80
print(p.score)
# del p.score
