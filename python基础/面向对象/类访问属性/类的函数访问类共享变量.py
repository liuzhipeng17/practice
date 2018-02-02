# -*- coding: utf-8 -*-

# __init__访问类共享变量的时候，要添加类名

# 统计实例化了多少个对象

class Student(object):
    country = 'China'
    n = 0

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Student.n += 1  # 在类中访问共享变量的时候，要添加类名；
        # 因为n只在内存中存储一份，所有的修改和访问都是到这一段内存做处理


print(Student.n)
s = Student('lzp0', 'male')
print(Student.n) #也可以是s.n
s1 = Student('lzp1', 'male')
print(Student.n)# 也开始s.n或者s1.n
s2 = Student('lzp2', 'male')
print(Student.n)