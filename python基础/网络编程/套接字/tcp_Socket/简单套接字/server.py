# -*- coding: utf-8 -*-

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 买手机
phone.bind(('127.0.0.1', 8080)) # 插手机卡: ip和端口是元组，作为参数传给bind
# 绑定手机卡，告诉别人我的手机号
phone.listen(5) # 开机也称挂起连接（开启服务了，一次允许5个人打电话）

print('waiting calling')
conn, addr = phone.accept() # 等待别人电话，conn：线路， addr:客户端手机号

print('phone con: %s' % conn)
print('client phone number:%s' % str(addr))
# addr类型是元组，必须要转成字符串，元组形式python2不支持打印

data = conn.recv(1024)

print('client sent: %s ' % data)

conn.send(data.upper())

conn.close() # 挂电话
phone.close()
