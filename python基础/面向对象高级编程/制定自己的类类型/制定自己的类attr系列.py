# coding= utf-8


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        print("call __setattr__")
        # self.key = value # 这一句会造成无穷递归，因为这一句等效：self.name = name
        # 正是self.name = name 触发了__setattr__（self,key,value)的执行
        self.__dict__[key] = value
        # setattr(self, key, value) 也是造成无穷递归，等效self.key = value

    def __delattr__(self, item):
        # del f1.age会触发__delattr__执行， item是字符串
        print("call __delattr__")
        self.__dict__.pop(item)

    def __getattr__(self, item):
        print("call __getattr__")
        # 当找不到属性，会触发
        # 当属性存在__dict__时，不会触发
        value = 5
        setattr(self, item, value)
        return value


# 测试getattr
# f = Foo('egon')
# print('before %s'% f.__dict__)
# print(f.data)
# print('after %s'% f.__dict__)
# print(f.data) # 此时调用的不是__getattr__，而是直接从dict获取

#测试setattr
f = Foo('egon') # 初始化有一个self.name = name就会调用__setattr__
print('before %s'% f.__dict__)
f.name = 'lzp' # 会调用__setattr__
print('after %s'% f.__dict__)
print(f.data) # 从f.__dict__查找属性，而且从父类也找不到；触发__getattr__