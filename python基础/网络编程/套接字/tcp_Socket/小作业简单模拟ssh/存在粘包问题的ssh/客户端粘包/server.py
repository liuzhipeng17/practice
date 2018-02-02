# -*- coding: utf-8 -*-

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)

print('waiting calling')
conn, addr = phone.accept()

data = conn.recv(1024)

print('包: %s ' % data)



