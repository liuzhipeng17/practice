# -*- coding: utf-8 -*-

import gevent
import time


def A():
    for _ in range(5):
        print('-------A-------', time.ctime())
        gevent.sleep(4) # 用来模拟一个耗时操作，注意不是time模块中的sleep


def B():
    for _ in range(3):
        print('-------B-------', time.ctime())
        gevent.sleep(1)  # 每当碰到耗时操作，会自动跳转至其他协程,是由gevent切换，不是操作系统

# g1 = gevent.spawn(A) # 创建一个协程
# g2 = gevent.spawn(B)
# g1.join()  # 等待协程执行结束
# g2.join()

# 上面的四条语句可以用一下代替
gevent.joinall([
    gevent.spawn(A),
    gevent.spawn(B),
])