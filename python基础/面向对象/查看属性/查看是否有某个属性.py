# -*- coding: utf-8 -*-


class Student(object):
    country = 'China'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def search_score(self):
        print('hello')

s = Student('lzp', 'male')

print(dir(s))

# 查看某个对象是否具有某个属性
print(hasattr(s, 'country'))
# 获取某个属性
print(getattr(s, 'country'))
# 设置某个属性
setattr(s, 'country', 'India')
# 再次查看country属性
print(getattr(s, 'country'))