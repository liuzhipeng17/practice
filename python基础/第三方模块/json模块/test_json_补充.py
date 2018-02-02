# -*- coding: utf-8 -*-

import json

# d = "{'name':'egon'}"
# 会报错，因为str(d)不是符合json格式的字符串，
# json格式的字符串里面的引号必须是双引号
d = '{"name":"egon"}'
# 必须是d = '{"name":"egon"}'这种形式，否则不认为是json的字符串
# d = {"name":"egon"}
# d = str(d)
ret = json.loads(str(d))
print ret["name"]

