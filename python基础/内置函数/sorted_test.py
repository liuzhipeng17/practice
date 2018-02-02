# coding= utf-8
# 默认是按照升序排列，得到的是一个列表
# reverse=True是按降序排列
s = 'hello'
print sorted(s)
print sorted(s, reverse=True)

# def sorted(iterable, cmp=None, key=None, reverse=False):

#     """ sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list """
#     pass


salary = {'alex': 20000,
          'wupeiqi': 2000,
          'egon': 5002}
# 默认是根据key排序
print sorted(salary)
# ['alex', 'egon', 'wupeiqi']
# 按照工资进行排序，得到的是升序排列的名字列表
print sorted(salary, key=(lambda x: salary[x]))
# 结果为['wupeiqi', 'egon', 'alex']


