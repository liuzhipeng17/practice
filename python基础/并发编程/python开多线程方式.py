# -*- coding: utf-8 -*-


import threading
import time


def music(name):
    print("begin listen music {name}: {time}".format(name=name, time=time.ctime()))
    time.sleep(6) # 模拟阻塞iO操作
    print("end listening {time}".format(time=time.ctime()))


def network(name):
    print("begin network {name}: {time}".format(name=name, time=time.ctime()))
    time.sleep(3) # 模拟阻塞iO操作
    print("network end {time}".format(time=time.ctime()))

# 从这开始都是主线程
threads = []
t1 = threading.Thread(target=music, args=("love",))
t2 = threading.Thread(target=network, args=("shopping",))
threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()
#
# t1.join() # 等待t1结束才继续执行主线程，主线程阻塞在这，等待t1结束，才会执行t2.join()
# t2.join() # 等待t2结束才继续执行主线程，(t2耗时比t1少）

# 执行完t1后, 发现t2已经执行完了，所以t2.join()就不会阻塞主线程，主线程继续执行print
print("all over {}".format(time.ctime()))