# -*- coding: utf-8 -*-
from greenlet import greenlet
import time

def A():
    while 1:
        print('-------A-------')
        time.sleep(0.5)
        g2.switch()# 跳转协程g2

def B():
    for _ in range(3):
        print('-------B-------')
        time.sleep(0.5)
        g1.switch()# 跳转协程g1

g1 = greenlet(A)  #创建协程g1
g2 = greenlet(B)

g1.switch()  #跳转至协程g1

# greenlet不好的地方是：需要人为的指定跳转的地方

