# re.search 和re.match返回的对象是match object

# match.group() 无命名分组
import re

m = re.match(r"(\w+) (\w+)", "%Isaac Newton, physicist")
print(m)
# None
m = re.search(r"(\w+) (\w+)", "%Isaac Newton, physicist")
print(m)
# <_sre.SRE_Match object; span=(1, 13), match='Isaac Newton'>
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(1,2))

# 命名分组(?P<name>pattern)
m = re.search(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group("first_name"))
print(m.group("last_name"))

