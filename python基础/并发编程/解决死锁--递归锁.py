# -*- coding: utf-8 -*-

import threading
import time

# mutexA = threading.Lock()  # Lock是一个类
# mutexB = threading.Lock()

recur_lock = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self):
        # threading.Thread.__init__(self)
        super().__init__()  # 这里不要self参数，只要除去self外的参数

    def run(self):
        # 当调用实例化对象的start()函数时，会调用run函数
        self.fun1()
        self.fun2()

    def fun1(self):
        recur_lock.acquire()
        print("I am {name}, get res:{res}->{time}".format(name=self.name, res="ResA", time=time.ctime()))
        recur_lock.acquire()
        print("I am {name}, get res:{res}->{time}".format(name=self.name, res="ResB", time=time.ctime()))
        recur_lock.release()
        recur_lock.release()

    def fun2(self):
        recur_lock.acquire()
        print("I am {name}, get res:{res}->{time}".format(name=self.name, res="ResB", time=time.ctime()))
        time.sleep(0.1)  # 加上这一行，会产生死锁
        recur_lock.acquire()
        print("I am {name}, get res:{res}->{time}".format(name=self.name, res="ResA", time=time.ctime()))
        recur_lock.release()
        recur_lock.release()


if __name__ == "__main__":
    for _ in range(10):
        t = MyThread()
        t.start()

# 递归锁threading.RLock()，每当acquire()一次，计数器+1,每当release一次，计数器-1
# 当一个线程获取到递归锁后，其他线程是无法再获取递归锁（这和普通锁是一样的）
# 但是递归锁可以被同一个线程多次acquire()(这是和普通锁不一样的地方）
# 只有当计数器为0的时候，其他线程才能acquire这把锁