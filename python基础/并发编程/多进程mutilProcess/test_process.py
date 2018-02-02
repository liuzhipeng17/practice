# -*- coding: utf-8 -*-

import time
import multiprocessing


def f(name):
    print('hello', name, time.ctime())
    time.sleep(1)

process_list = []
for i in range(1):
    # t = threading.Thread(target=subnum)
    t = multiprocessing.Process(target=f, args=("lzp_%s"%i,))
    t.start()
    process_list.append(t)

for t in process_list:
    t.join()

print("end {datetime}".format(datetime=time.ctime()))

