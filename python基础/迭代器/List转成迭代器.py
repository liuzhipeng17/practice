from collections import Iterator

l = [1, 2, 3]
s = iter(l)
print(isinstance(s, Iterator))