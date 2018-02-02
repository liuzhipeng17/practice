# coding= utf-8


class Student(object):
    country = 'China'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


s = Student('lzp', 'male')


# 查看类的命名空间（存放类的属性的容器）
print Student.__dict__
# 查看对象的命名空间
# print s.__dict__


# 查找country属性# 查找s.country时，会先在s.__dict__里面查找，找不到会去Student.__dict__查找
# print s.country


# country属于类变量，存储在Student.__dict__中