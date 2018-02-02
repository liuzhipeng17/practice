
# -*- coding: utf-8 -*-
import subprocess

sp = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# sp.universal_newlines = False
(out, err) = sp.communicate() # 这样是阻塞的,一直在等子进程结束，它的父进程为python解析器

print(type(out))
print(type(err))
# print sp.stdout # 是一个文件句柄，读取方式为rb
# <open file '<fdopen>', mode 'rb' at 0x01381910>
# data = sp.stdout.read()
# 这个是byte格式，需要解码，解码格式和操作系统有关
# 如果是windows，要gbk,如果是linux？
# print type(data) # 在Python 2.7 str包含byte 普通的str
# print out.decode('gbk')
# print err.decode('gbk')
