# -*- coding: utf-8 -*-
# 反射：通过字符串的形式访问对象（模块对象，类和类实例化对象）的属性


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
print(hasattr(s, 'country')) # 在dir(）列表里面查找是否有country这个元素
# 获取某个属性
print(getattr(s, 'country'))
# 设置某个属性
setattr(s, 'country', 'India')
# 再次查看country属性
print(getattr(s, 'country'))

print(getattr(s, 'cc', '属性不存在'))# 当属性不存在时，会返回字符串“属性不存在”