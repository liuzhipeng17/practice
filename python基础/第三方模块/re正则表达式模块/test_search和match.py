# -*- coding: utf-8 -*-

# re.search(pattern, string, flag=0)
# 扫描字符串, 查找正则表达式第一次匹配成功的位置，并返回一个匹配对象match object;
# 如果字符串没有匹配成功，则返回None
# match group()方法拿到匹配结果

# re.match只在字符串的开头匹配，re.search是在字符串的任意位置匹配

import re

m = re.search(r"c", "abcdef" )
print(m)
# <_sre.SRE_Match object; span=(2, 3), match='c'>

m = re.match(r"c", "abcdef")
print(m)
# None
# 按出现的模式来拆分字符串。如果在模式中使用捕获括号，
# 那么模式中的所有组的文本也作为结果列表的一部分返回。
# 如果maxsplit是非零，那么在大多数maxsplit拆分发生时，
# 将返回字符串的其余部分作为列表的最后一个元素。


#match和search比较
#match只在字符串开头进行匹配，无论是多行还是一行字符串，不会第二行开始匹配，
# search会在每一行进行匹配

m = re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
print(m)
# None
m = re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match
print(m)
# <_sre.SRE_Match object; span=(4, 5), match='X'>