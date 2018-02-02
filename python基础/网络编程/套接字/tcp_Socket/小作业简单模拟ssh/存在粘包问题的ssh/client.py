# -*- coding: utf-8 -*-

import sys
print(sys.getdefaultencoding())  # python3 默认编码是utf-8;python2默认编码是ascii
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))
while True:
    msg = input("input msg>>> ").strip()
    if not msg:
        continue
    phone.send(msg.encode(encoding='utf-8'))
    data = phone.recv(1024)
    print("服务端返回内容：%s" % data.decode('gbk'))

phone.close()

# 这个程序是存在粘包的问题，所以要自定义报头：
# 报头（固定长度的bytes,描述数据的长度）
# struct.pack('i',len(data)) 发送方，先发报头，再发数据
# 接收方先接受固定长度的报头，然后循环接受