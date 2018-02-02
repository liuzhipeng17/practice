
# -*- coding: utf-8 -*-
import subprocess
import time

proc = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# (out, err) = sp.communicate() # 这样是阻塞的
while proc.poll() is None: # 注意不要写成while proc.poll() 0和None定义不一样
    time.sleep(0.005)
    print "执行其他动作，在这里可以干其他事情"
print 'Exist status %s' % proc.poll()

# print sp.stdout # 是一个文件句柄，读取方式为rb
# <open file '<fdopen>', mode 'rb' at 0x01381910>
data = proc.stdout.read()
# 这个是byte格式，需要解码，解码格式和操作系统有关
# 如果是windows，要gbk,如果是linux？
# print type(data) # 在Python 2.7 str包含byte 普通的str
print data.decode('gbk')
