

class A(object):
    def outer(func):
        def inner(self):
            print("222")
            r=func(self)
            print("3333")
            # return r
        return inner

    @outer  # f = outer(f),执行outer函数，得到函数，然后赋值给f
    def f(self):
        print("000")

obj = A()
obj.f()