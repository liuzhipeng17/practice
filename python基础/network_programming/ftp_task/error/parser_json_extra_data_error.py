import json

decstr='{"colspan":2,"title":{"data":23}, "align":"center\n"}'
#  必须为单引号字符串，里面的属性，值必须为双引号
# decstr="".join([decstr.strip().rsplit("}", 1)[0], "}"])
print(decstr[51])
json_dict = json.loads(decstr)
print(json_dict)
str_temp = json.dumps(json_dict)
print(str_temp)

