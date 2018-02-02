# -*- coding: utf-8 -*-

# import socket
import socketserver


server_addr = ('127.0.0.1', 8080)

class MyUdpServer(socketserver.BaseRequestHandler):
    def handle(self):

        msg, socket_obj = self.request # 这里已经包含接收消息了
        print("接收到客户端%s消息：%s" % (self.client_address, msg.decode('utf-8')))
        send_msg = input(">>>")
        socket_obj.sendto(send_msg.encode('utf-8'), self.client_address)


        # while True: # 通信循环
        #     socket_obj.recvfrom(1024)
        #     print("接收到： %s" % data.decode('utf-8'))
        #     print("客户端地址： %s" % str(client_addr))
        #     msg = input(">>>").encode('utf-8')
        #     socket_obj.sendto(msg, client_addr)

if __name__ == "__main__":
    obj = socketserver.ThreadingUDPServer(server_addr, MyUdpServer)
    obj.serve_forever()