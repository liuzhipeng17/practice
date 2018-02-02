# -*- coding: utf-8 -*-

import sys
# print(sys.getdefaultencoding())  # python3 默认编码是utf-8;python2默认编码是ascii
import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))
while True:
    msg = input("input msg>>> ").strip()
    if not msg:
        continue
    phone.send(msg.encode(encoding='utf-8'))

    # part1: 先接报头长度
    head_bytes_len_bytes = phone.recv(4)
    head_bytes_len_int = struct.unpack('i', head_bytes_len_bytes)[0]

    #part2: 接报头
    head_bytes = phone.recv(head_bytes_len_int)
    head_str = head_bytes.decode('utf-8')
    head_dict = json.loads(head_str)
    data_size = head_dict['data_size']

    # 最后接收数据
    recv_data = b''
    recv_size = 0
    while recv_size < data_size:
        data = phone.recv(1024)
        recv_size += len(data)
        recv_data += data
    print("服务端返回内容：%s" % recv_data.decode('gbk')) # 如果服务端是linux，改成utf-8

phone.close()

# 这个程序是存在粘包的问题，所以要自定义报头：
# 报头（固定长度的bytes,描述数据的长度）
# struct.pack('i',len(data)) 发送方，先发报头，再发数据
# 接收方先接受固定长度的报头，然后循环接受