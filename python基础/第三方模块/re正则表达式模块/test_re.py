# -*- coding: utf-8 -*-

import re
s = re.findall(r'(ad)+yuan', 'adadyuanddd')
print(s)
# 返回结果为['ad']
print(re.findall(r'(?:ad)+yuan', 'adadyuanddd'))
# 返回结果为['adadyuan']

print(re.findall('c\\\\l','cc\l'))
# python解析器，re正则表达式
# python将c\\\\l 翻译成c\\l
# re 正则表达式得到c\\l,所以能匹配成功
print(re.findall(r'c\\l', 'cc\l'))
# r是告诉Python解析器，不要转义里面东西，原样交给re
# 在re里面\有特殊意义，所以要\\变成普通字符

print(re.findall("\dI", "hello 654I am LIA"))
# python不认识\d，但是会认识\b（在python解析器会认为特殊功能）
# 上面的结果是：['4I']
# 为了避免python解析器不必要的转义，添加r

ret = re.match("\d+", "dj44jg")
print(ret)

# re.split() 得到列表
print(re.split('\d+', 'fhd3245skf54skf453sd'))
print(re.split('l','hello, lzp'))

# re.sub

# re.compile

pattern = re.compile('\d+')
print(pattern)
s = pattern.findall("hello2344")
print(s)
print(re.findall(r'(?P<author>\w+)\.articles\.(?P<id>\d+)','yuan.articles.1234'))
s = re.search(r'(?P<author>\w+)\.articles\.(?P<id>\d+)','yuan.articles.1234')
print(s.group())
print(s.groupdict())
print(s.group('id'))
print(s.group('author'))

print(re.findall(r'\d+', 'bd125bd5454adfd'))