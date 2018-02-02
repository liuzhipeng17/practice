# -*- coding: utf-8 -*-

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))
while True:
    msg = raw_input("input msg>>> ").strip()
    if not msg:
        continue
    phone.send(msg)
    data = phone.recv(1024)
    print "服务端返回内容：%s" % data

phone.close()