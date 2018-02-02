# -*- coding: utf-8 -*-

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 买手机
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 重用端口
phone.bind(('127.0.0.1', 8080)) # 插手机卡: ip和端口是元组，作为参数传给bind
phone.listen(5) # 开机
print 'waiting calling'
while True:
    conn, addr = phone.accept() # 等待别人电话，conn：线路， addr:客户端手机号
    print 'phone con: %s' % conn
    print 'client phone number:%s, type(addr):%s' % (str(addr),type(addr))
    # addr类型是元组，必须要转成字符串，元组形式python2不支持打印
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break # 兼容linx服务端在客户端断开连接后不会报异常，而是一直接受空消息
            print 'client sent: %s ' % data
            conn.send(data.upper())
        except Exception:
            break # 兼容windows服务器，在客户端断开连接后会抛出异常ConnectResetError

    conn.close() # 挂电话
phone.close()
