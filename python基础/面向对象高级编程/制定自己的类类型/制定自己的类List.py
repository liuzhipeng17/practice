# -*- coding: utf-8 -*-


class List(object):
    def __init__(self, x):
        self.seq = list(x)

    def append(self, value):
        if not isinstance(value, str):
            raise TypeError('must be a str')
        self.seq.append(value)

    @property
    def mid(self):
        index = len(self.seq)//2
        return self.seq[index]

    def __getattr__(self, item):
        return getattr(self.seq, item)

    # 控制打印行为
    def __str__(self):
        return str(self.seq)


l = List([1,2,3])
print(l) # 如果没有__str__，就必须是print l.seq
l.append('4')
print(l)
l.insert(0, 0)
print(l)