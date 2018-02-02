# -*- coding: utf-8 -*-


import threading
import time


def music(name):
    print("begin listen music {name}: {time}".format(name=name, time=time.ctime()))
    time.sleep(6) # 模拟阻塞iO操作
    print("end listening {time}".format(time=time.ctime()))


def network(name):
    print("begin network {name}: {time}".format(name=name, time=time.ctime()))
    time.sleep(4) # 模拟阻塞iO操作
    print("network end {time}".format(time=time.ctime()))

# 从这开始都是主线程
threads = []
t1 = threading.Thread(target=music, args=("love",))
t2 = threading.Thread(target=network, args=("shopping",))
threads.append(t1)
threads.append(t2)

t2.setDaemon(True)
# 将t2设置为守护线程，当主线程结束后，就会等t2的结束；此时t1还在运行，
# t2.setDaemon(True)

for t in threads:
    t.start()

print("all over {}".format(time.ctime()))
# 到这里，主线程不一定就结束了：还要看它的所有非守护线程是否都结束了
# 当主线程的所有非守护线程都结束了，才认为主线程结束了
# 类方法：
# threading.enumerate() #计算当前正在运行的所有线程

# 守护线程的作用：监听