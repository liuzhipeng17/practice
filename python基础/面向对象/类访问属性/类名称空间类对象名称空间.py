# coding= utf-8


class Student(object):
    country = 'China'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


s = Student('lzp', 'male')
# g.__int__()
# 没有看到__init__的执行

# 查看类的命名空间（存放类的属性的容器）
print Student.__dict__
# 查看对象的命名空间
# print s.__dict__
# 奇怪的是country这个属性，在s.__dict__没有看见,但是在Student.__dict__
# 查找s.country时，会先在s.__dict__里面查找，找不到会去Student.__dict__查找
# print s.country

# country是类变量，所有对象共有的属性，不必实例化就可以访问，可以类访问，也可以用实例化对象访问

# 查看类属性
print Student.country

# 修改类的属性值
Student.country = "America"

# 增加类的属性
Student.sex_or_name = 'unkown'

# 可以看到类的名称空间里面增加了元素，'sex_or_name' = 'unkown'
print Student.__dict__


# 对象的名称空间只有自己的独有变量（不包含类变量）
print s.__dict__
#  {'name': 'lzp', 'sex': 'male'}
s.country = 'India'
# 上面的操作是增加s的属性，此时会在s.__dict__有’counttry':'India'
print s.__dict__
# country属性，不属于每个对象，属于类所有对象共享，
# 当共享对象为不可变类型是，对象修改共享对象，不会修改共享变量的值
# 当共享对象为可变类型时，对象修改共享对象，会修改共享变量的值
# s2 = Student()

