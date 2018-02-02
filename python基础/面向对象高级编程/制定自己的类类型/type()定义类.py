# -*- coding: utf-8 -*-

# 创建类的方法，除了用关键字class F(object)外，还有另外一种方法type()产生

# type称为元类， 类的类

# 创建类的三个要素：
# class_name 类名
# class_bases 类继承关系
# class_dict 类属性字典


def run(self):
    print('%s is runing' % self.name)

class_name = 'Bar'
class_dict = {
    'x': 1,
    'run': run,
}
class_bases = (object,)

Bar = type(class_name, class_bases, class_dict) # 这里不支持关键字传参
print(Bar) # Bar是一个类，不是实例化对象，
print(type(Bar))
print(Bar.__dict__)