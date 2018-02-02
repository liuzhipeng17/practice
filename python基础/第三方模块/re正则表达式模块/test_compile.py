# -*- coding: utf-8 -*-

# prog = re.compile(pattern)
# result = prog.match(string)
# 和下面的句子是等效的
# result = re.match(pattern, string)
# 但是，如果在单个程序中多次使用表达式，则使用re.compile()和保存生成的正则表达式对象以实现重用更为高效。

# re.I
# ignore case 忽略大小写

# re.M 多行匹配
# re.MULTILINE
# 指定时,模式字符“^”匹配字符串的开始和每一行的开头(每个换行后);
# 模式字符' $ '匹配在字符串末尾和每一行的末尾(在每个换行之前)。

# re.S 此时.会匹配包含换行符在内的任意字符


