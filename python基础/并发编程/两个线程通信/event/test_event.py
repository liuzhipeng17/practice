# -*- coding: utf-8 -*-

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(thread_name)-10s) %(message)s')
logger = logging.getLogger()


def worker(event):
    d = {"thread_name":threading.current_thread().name}
    logger.debug("waiting for redis ready [time:%s]",time.ctime(), extra=d)
    while not event.isSet():
        # 每隔3秒提示一下用户：状态
        event.wait(3)#
        logger.debug("waiting for redis ready %s", time.ctime(), extra=d)
    # wait()不加参数，会一直阻塞下去，知道event检测到变成True(不需要用户去检测）
    # wait(3)会阻塞3秒，无论如何都会执行下面的内容
    logger.debug("redis ready, and connect to redis, do some work [time:%s]", time.ctime(), extra=d)
    time.sleep(1)


def main():

    redis_ready = threading.Event() # 默认为False，
    t1 = threading.Thread(target=worker, args=(redis_ready, ), name="t1")
    t1.start()
    t2 = threading.Thread(target=worker, args=(redis_ready, ), name="t2")
    t2.start()
    d = {"thread_name": threading.current_thread().name}
    logger.debug("check redis whether is ready, and set True [time:%s]",time.ctime(), extra=d)
    time.sleep(6) #模拟去启动redis动作
    redis_ready.set()

if __name__ == "__main__":
    main()