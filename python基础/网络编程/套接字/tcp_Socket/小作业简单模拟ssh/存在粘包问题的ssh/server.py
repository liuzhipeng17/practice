# -*- coding: utf-8 -*-

import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 买手机
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8080)) # 插手机卡: ip和端口是元组，作为参数传给bind
phone.listen(5) # 开机
while True:
    print('waiting calling')
    conn, addr = phone.accept() # 等待别人电话，conn：线路， addr:客户端手机号
    print('phone con: %s' % conn)
    print('client phone number:%s' % str(addr))
    while True:
        try:
            cmd = conn.recv(1024).decode('utf-8') # 接收到的bytes，不需要转成str
            if not cmd:
                break
            print('client sent: %s ' % cmd)
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (out,err) = proc.communicate()

            conn.send(out)
            conn.send(err)
        except Exception:
            break

    conn.close() # 挂电话
phone.close()
