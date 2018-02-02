# -*- coding: utf-8 -*-

import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8080))
sock.listen(5) # 允许你多个客户端进行连接
select_list = [sock,]
print(sock)

while 1:
    r, w, e = select.select(select_list,[],[]) #
    # 监听sock套接字是否有变化（只有新客户端和server连接的时候，sock套接字有变化）
    print('r=',r)
    for socket_obj in r:  # r只能是sock或者conn1, conn2;但是sock是不变的
        if socket_obj == sock: # shitf+tab回退一个tab
            conn, addr = socket_obj.accept()
            print('conn={conn},  addr={addr}'.format(conn=conn, addr=addr))
            select_list.append(conn)
        # 将会监听conn套接字（只有在客户端和服务端进行通信（发消息）的时候，才会有变化）

        else:
            data = socket_obj.recv(1024)
            print("recv msg {msg}".format(msg=data.decode('utf-8')))
            send_data = input(">>>") #
            socket_obj.send(send_data.encode('utf-8'))
