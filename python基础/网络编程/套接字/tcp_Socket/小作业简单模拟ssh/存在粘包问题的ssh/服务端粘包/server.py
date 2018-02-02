# -*- coding: utf-8 -*-

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)

print('waiting calling')
conn, addr = phone.accept()

data1 = conn.recv(1)
data2 = conn.recv(1024)

print('第1个包: %s ' % data1)
print('第2个包: %s '  % data2)


