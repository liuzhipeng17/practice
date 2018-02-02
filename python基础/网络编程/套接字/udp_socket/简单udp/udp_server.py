# -*- coding: utf-8 -*-

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 8080)
socket.bind(server_addr)

while True: # 通信循环
    data, client_addr = socket.recvfrom(1024)
    print("接收到： %s" % data.decode('utf-8'))
    print("客户端地址： %s" % str(client_addr))
    msg = input(">>>").encode('utf-8')
    socket.sendto(msg, client_addr)

# 即使客户端发空，服务端不会卡在recvfrom哪里，因为udp会自动添加了报头