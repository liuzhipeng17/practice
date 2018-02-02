# -*- coding: utf-8 -*-

import threading
import time

mutexA = threading.Lock() # Lock是一个类
mutexB = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 当调用实例化对象的start()函数时，会调用run函数
        self.fun1()
        self.fun2()

    def fun1(self):
        mutexA.acquire()
        print("I am {name}, get res:{res}--->{time}".format(name= self.name, res="ResA", time=time.ctime()))
        mutexB.acquire()
        print("I am {name}, get res:{res}--->{time}".format(name=self.name, res="ResB", time=time.ctime()))
        mutexB.release()
        mutexA.release()

    def fun2(self):
        mutexB.acquire()
        print("I am {name}, get res:{res}--->{time}".format(name= self.name, res="ResB", time=time.ctime()))
        time.sleep(0.1) # 加上这一行，会产生死锁
        mutexA.acquire()
        print("I am {name}, get res:{res}--->{time}".format(name=self.name, res="ResA", time=time.ctime()))
        mutexA.release()
        mutexB.release()


if __name__ == "__main__":
    for _ in range(10):
        t = MyThread()
        t.start()