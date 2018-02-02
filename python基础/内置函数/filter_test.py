# coding= utf-8

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的时，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter(func, L)过滤掉L中不符合func的元素，保留符号func的元素
# python 2返回的是List, python返回的是一个可迭代对象

d = [{'name': 'lzp', 'age': 20},
     {'name': 'egon', 'age': 30 },
     {'name': 'alex', 'age': 50 }
     ]
f = filter(lambda d: d['age'] > 20, d)
print f