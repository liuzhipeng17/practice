# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(5) # 允许你多个客户端进行连接

while 1: # 连接循环，但是会发现，一个连接进去出不来，所以只能有一个连接可以进行通信
    conn, addr = sock.accept()
    print("server working, and client is", addr)

    while 1: # 通信循环
        recv_data = conn.recv(1024)  # 记住这里是conn，不是sock
        if not recv_data:
            break
        print("recv_data", recv_data.decode('utf-8'))
        send_data = input(">>>")
        conn.send(send_data.encode('utf-8'))

    conn.close()

sock.close()

# 上面的程序存在问题：server虽然可以连接多个客户端，但是只有一个客户端，能够和服务端进行通信
# 因为只有一个连接能够进去到链接循环，而且出不来。 