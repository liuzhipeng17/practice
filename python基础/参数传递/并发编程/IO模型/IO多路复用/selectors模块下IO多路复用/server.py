# -*- coding: utf-8 -*-

import selectors
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8080))
sock.listen(5) # 允许你多个客户端进行连接

multiplex = selectors.DefaultSelector() # 根据平台选择最佳io多路复用机制（linux:epoll, windows:select)


def comm(conn, mask):
    try:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            multiplex.unregister(conn)
        else:
            print(recv_msg.decode('utf-8'))
            send_msg = input(">>>")
            conn.send(send_msg.encode('utf-8'))
    except Exception:
        multiplex.unregister(conn)


def accept(file_obj, mask):
    conn, addr = file_obj.accept()
    print("conn={conn}".format(conn=conn))
    multiplex.register(conn, selectors.EVENT_READ, data=comm)

multiplex.register(sock, selectors.EVENT_READ, data=accept)
# 注册并不是监听，注册定义了一些事件：会监听sock的变化，sock为fd, data为fd绑定的回调函数

while 1:
    print("waiting")
    event_list = multiplex.select()# 监听所有注册对象，当对象变化，会触发执行data
    print(event_list)
    for key, mask in event_list: # 当前活动的对象们
        print(key)
        # SelectorKey对象，是一个元组，
        # key.fileobj是当前活动的socket对象，
        # key.data是对应fd绑定的回调函数
        callback = key.data
        callback(key.fileobj, mask)



