# -*- coding: utf-8 -*-
import re

# 首先要知道贪婪匹配有哪些字符产生的：
# *，？，+，  {n,}, {m,n} 这些会产生贪婪匹配

a = 'aacbacbc'
reg = r'a.*b'
s = re