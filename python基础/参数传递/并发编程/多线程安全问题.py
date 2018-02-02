# -*- coding: utf-8 -*-

import time
import threading

num = 100

def subnum():
    global num
    temp = num
    time.sleep(0.001)
    num = temp -1

threads = []
for _ in range(100):
    t = threading.Thread(target=subnum)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("最后num={nums}".format(nums=num))

