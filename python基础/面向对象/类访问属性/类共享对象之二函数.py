# -*- coding: utf-8 -*-

# 类对象的名称空间只有变量，没有函数
# 所有函数是所有类对象共享的


class Student(object):
    country = 'China'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def search_score(self):
        print('hello')

s = Student('lzp', 'male')
print(s.__dict__)
# {'name': 'lzp', 'sex': 'male'}
print(Student.search_score)
# <unbound method Student.search_score>
# 未绑定方法
print(s.search_score)
# <bound method Student.search_score of <__main__.Student object at 0x02A280F0>>
# 绑定方法
# 将方法绑定到对象

s.search_score() # 等效于Student.search_score(s)
Student.search_score(s)