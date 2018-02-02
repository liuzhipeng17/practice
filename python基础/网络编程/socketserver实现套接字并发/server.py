# -*- coding: utf-8 -*-


import socketserver


class TcpServer(socketserver.BaseRequestHandler): # 通信循环
    def handle(self):
        print(self.request)  # self.request 等效于 accept(),建立连接
        while True:
            data_recv = self.request.recv(1024)
            print(data_recv)
            msg_send = input(">>>>").encode('utf-8')
            self.request.send(msg_send)


if __name__ == "__main__":
    obj = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), TcpServer)
    obj.serve_forever()
    ## 开辟了多个线程（多个服务员）ThreadingTcpServer
    # 每个服务员，循环利用（多次循环链接） obj.server_forserver()
    # 每个链接里面，循环提供服务（TcpServer)



# 这个例子还存在问题：客户端可以练上去，但不能并发和服务端通信