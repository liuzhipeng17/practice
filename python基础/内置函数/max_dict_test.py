# coding= utf-8

# 比较字典中value值最大的key
# 比如比较工资最高的人

salary = {'alex': 20000,
          'wupeiqi': 2000,
          'egon': 5002}

print max(salary)
"""max(iterable[, key=func]) -> value"""
# max 默认字典的时候，是根据key进行比较，返回的是key
# 需要添加key参数，指明根据什么进行比较，返回的还是key
# 需求是根据字典的value进行比较，所以key = lambda x : salary[x]
# 这个x,是由salary提供即for i in salary 中 的i

print max(salary, key=(lambda x: salary[x]))