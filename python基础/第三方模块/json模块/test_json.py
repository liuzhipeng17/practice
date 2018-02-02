# -*- coding: utf-8 -*-

# d = {"河北":["廊坊","保定"], "湖南":["长沙","韶山"]}
# s = eval(str(d))
# print s["河北"]
# eval最重要的是完成数学计算

# json是连接两种不同语言的桥梁，json和文件没有关系
# 序列化：把对象从内存变成可存储或传输的过程称为序列化

import json

d = {'name': 'egon'}
# 序列化，将d转换成一个字符串
s = json.dumps(d)
with open('new.txt','w+') as f:
    f.write(s)

# 上面等效：
# with open('new2.txt','w') as f:
#     json.dump(d, f)

# 反序列化
with open('new.txt','r') as f:
   data = f.read()
   #反序列化，将字符串数据还原成相应的格式
   data2 = json.loads(data)
   print(data2["name"])
