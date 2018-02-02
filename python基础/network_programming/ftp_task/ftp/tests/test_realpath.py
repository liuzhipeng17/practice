import os.path


a = os.path.join(os.path.abspath(__file__))
print(a)
b = os.path.normpath('..\\..\\tests')
print(b)
c = os.path.join(a,b)
print(c)
d = os.path.realpath(c)
print(d)
b = '..\\..\\tests'
e = b.replace

