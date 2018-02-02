# -*- coding: utf-8 -*-

import hashlib

m = hashlib.md5()
m.update('admin')    # 534b44a19bf18d20b71ecc4eb77c572f 是对一个alex
m.update('12345')    # 0bf4375c81978b29d0f546a1e9cd6412 是对两个alexalex
print(m.hexdigest())


def calc_md5(password, name):
    m = hashlib.md5()
    m.update(password + name)
    return m.hexdigest()

print(calc_md5('admin', '12345'))