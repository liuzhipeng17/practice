# -*- coding: utf-8 -*-

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 8080)
while True:
    msg = input("msg: ").encode('utf-8')
    socket.sendto(msg, server_addr)
    recv_msg, server_addr = socket.recvfrom(1024)
    print(recv_msg.decode('utf-8'))


