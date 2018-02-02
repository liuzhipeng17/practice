# -*- coding: utf-8 -*-

# 自己定义一个类，写内容，会将当期时间写进去

from time import localtime, strftime


class Foo(object):
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        print("enter exec")
        return self
# 要return self, 不要return self.f ,不然调用f.write 会调用真正内置的write， 而不是类定义的write

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit exec")
        print('exc_type= %s, exc_val= %s, exc_tb= %s' % (exc_type, exc_val, exc_tb))

# 要使用with，类定义必须包含__enter__和__exit__缺一都会报异常
with Foo('a.txt', 'w+') as ff:
    # with 一个对象，会触发该对象的__enter__的执行
    # as f 会将__enter__返回值赋给f（ as f可选），如果没有return语句，f = None

    # 接下来，会执行子代码；
    # 如果子代码有抛出异常，退出子代码的执行，会触发__exit__
    # 子代码抛出的异常，需要在__exit__进行处理
    # 如果__exit__的返回值为True，程序接着运行（退出子代码后的点）
    print('with Foo的子代码')
    raise NameError("命名错误")

print('end')