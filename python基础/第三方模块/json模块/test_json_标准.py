# -*- coding: utf-8 -*-

import json

# s = json.dumps([1, 2, 3,{'4':5, '6':7}]) # 不紧凑的json
# [1, 2, 3, {"4": 5, "6": 7}]
s = json.dumps([1, 2, 3,{'4':5, '6':7}], separators=(',', ':')) # 紧凑的json，会将空格等去掉
# [1,2,3,{"4":5,"6":7}]
print(s)