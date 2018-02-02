# -*- coding: utf-8 -*-

import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))

phone.send('hello'.encode(encoding='utf-8'))
phone.send('world'.encode(encoding='utf-8'))

# data = phone.recv(1024)

# print("服务端返回内容：%s" % data)
# phone.close()