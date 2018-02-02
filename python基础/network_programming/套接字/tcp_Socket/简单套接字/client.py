# -*- coding: utf-8 -*-

import socket
import time

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))
# time.sleep(2)
phone.send('hello')

data = phone.recv(1024)

print "服务端返回内容：%s" % data
phone.close()