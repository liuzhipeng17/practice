# -*- coding: utf-8 -*-

import random

# 5位随机字符串,由数字0-9和字母a-z A-Z组合(产生一个二维码）


def validate():
    s = ''
    for i in range(5):
        random_number = str(random.randint(0,9))
        random_str = chr(random.randint(0, 25) + random.choice([65,97]))
        random_s = random.choice([random_number, random_str])
        s += random_s

    return s

# print validate()

# print random.choice(['abdd', 'addd'])