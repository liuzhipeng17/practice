# -*- coding: utf-8 -*-

import time
import threading

num = 100


def subnum():
    global num
    print('ok') # 这里还是同时出来，
    # 对下面操作进行枷锁，同时只允许一个线程进来操作
    # 锁内的操作就破坏了多线程的并发性
    lock.acquire()
    temp = num
    time.sleep(0.001)
    num = temp -1
    lock.release()

threads = []
lock = threading.Lock()
for _ in range(100):
    t = threading.Thread(target=subnum)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("最后num={nums}".format(nums=num))

