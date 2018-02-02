# coding= utf-8

# map(func, iter1）

L = [1,2,3]
m = map(lambda x: x**2, L)
# x的实参是for i in L中的i
# 字典的是for k in L此时的k 为Key
print(m, type(m), list(m))


L = [1,2,'a']
m = map(str, L)
m = list(m)
print(m)
# 将列表元素转成字符
# 下面实现将列表转成字符串, 要求join(self,iterable),iterable里面的元素必须是字符
w = "".join(m)
print(w, type(w))


# python3有点不一样，返回的是可迭代器，不是list

# 规范名字的输入：['AdM', 'LisA','barT']变成['Adm', 'Lisa', 'Bart']
# str.capitalize()将字符串（没有要求是纯字母），第一个元素为大写，其余均小写

s = '2AD22Ms'
print(s.capitalize())

L = ['ADm', 'LisA', 'BaRt']
m = map(lambda x: x.capitalize(), L)
print(list(m))
# 只要记住，x 是for i in L中的i即可

li = [{'class_id': 2}, {'class_id': 3}, {'class_id': 6}]

m = map(lambda  x:x['class_id'], li)
print(list(m))