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
print(Student.__dict__)
# 查看对象的命名空间
print(s.__dict__)
# 奇怪的是country这个属性，在s.__dict__没有看见
# print s.country
