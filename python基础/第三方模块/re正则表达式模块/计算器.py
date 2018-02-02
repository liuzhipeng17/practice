# -*- coding: utf-8 -*-

import re

s = "1 -2 * (  (60 -30 +(-40 + 5) * 5) +3)"
s = s.replace(" ", "") # // 会删除所有空格，即使一个空白段是多个空白字符组成
print(s)
# def format(s):
#     # s.replace("+-","-")
#     # s.replace("--", "+")
#     pass
#


def calc(str):
    pass
    return
    # 加减乘除方法 后缀表达式来计算
pattern = r'\([^()]+\)'
while re.search(pattern, s):
    match_str = re.search(pattern, s).group()
    cal_value = calc(match_str)
    s = re.sub(pattern, cal_value, s, 1)

