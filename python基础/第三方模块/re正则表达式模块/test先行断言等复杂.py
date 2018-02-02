# -*- coding: utf-8 -*-

import re

m = re.findall(r'\bfoo\b', "foo bar foo bar (foo3)")
print(m)
# ['foo', 'foo']
# (foo3)没有匹配到

# 先行断言： 如果Isaac接下来是Asimov就会匹配Isaac
# (?=)
m = re.findall(r'Isaac(?=Asimov)',"IsaacAsimov")
print(m)

m = re.findall(r'\d+(?=\s+foo\s*)',"12 foo")
print(m)

# (?!)  如果Isaac接下来不是Asimov就会匹配Isaac
m = re.findall(r'Isaac(?!Asimov)',"Isaacadfdf")
print(m)

# 向后断言，和(?=)相反，匹配后面
# 如果def前面跟着的是abc，则会匹配def
m = re.findall('(?<=cc)def', 'abcdef')
print(m)

# 如果-后面跟着的是数字或字母，则会匹配后面的数字或者字母
m = re.search('(?<=-)\w+', 'spam-55')
print(m.group(0))

