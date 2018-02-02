# -*- coding: utf-8 -*-

import socket
import subprocess
import time


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)
print 'waiting calling'
while True: #连接循环
    conn, addr = phone.accept()
    print 'phone con: %s' % conn
    print 'client phone number:%s' % str(addr)
    # addr类型是元组，必须要转成字符串，元组形式python2不支持打印
    while True: # 通信循环
        try:
            cmd = conn.recv(1024)
            if not cmd:
                break
            print 'client sent: %s ' % cmd
            sp = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (out, err) = sp.communicate()
            # while sp.poll() is None:
            #     time.sleep(0.1)
            #     print "子进程还没结束" # 这种方式是不推荐的，因为当输出比较大时，会卡死
            # out = sp.stdout.read()
            # err = sp.stderr.read()
            conn.send(out) # send 发送的就是byte
            conn.send(err)
        except Exception:
            break
    conn.close() # 挂电话 end

phone.close()
