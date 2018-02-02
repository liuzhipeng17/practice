# -*- coding: utf-8 -*-

from time import localtime, strftime


class Open(object):
    def __init__(self, file_path, mode='r'):
        print("exec __init__")
        self.f = open(file_path, mode=mode)

    def __getattr__(self, item):
        print('exec __getattr__')
        return getattr(self.f, item)
        # getattr中的self.f是一个对象,找不到属性，从原有的open对象获取

    # 析构函数，当代码执行完或者 del 实例化对象时，会触发__del__执行
    # 该函数的作用：清理资源（关闭文件，浏览器，关闭数据库连接等）
    def __del__(self):
        print('exec __del__')
        self.f.close()

f = Open('get_attr.txt', 'a+')
f.write('123654\n') # 找不到属性，会会触发__getattr__
f.seek(0)          # 找不到属性，会触发__getattr__,
print(f.read())   # 找不到属性，会触发__getattr__
# 代码执行完会触发__del__的执行

# 运行结果：
# exec __init__
# exec __getattr__
# exec __getattr__
# exec __getattr__
# 123654
# 123654
# exec __del__