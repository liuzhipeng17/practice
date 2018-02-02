# coding= utf-8

# zip 多个可迭代对象同时跑，然后各自的值组合起来

# 长度不对等情况
L1 = [1, 2, 3]
L2 = 'abcd'
z = zip(L1, L2)
print(list(z))
# 输出[(1, 'a'), (2, 'b'), (3, 'c')]

# 长度对等
L1 = [1, 2, 3]
L2 = 'ccd'
z = zip(L1, L2)
print(list(z))

# 输出[(1, 'c'), (2, 'c'), (3, 'd')]

# 变量zip生成器
name = ['Celia', 'Lisa', 'Marie']
len_name = [len(n) for n in name]
for name, len_name in zip(name, len_name):
    print(name, len_name)