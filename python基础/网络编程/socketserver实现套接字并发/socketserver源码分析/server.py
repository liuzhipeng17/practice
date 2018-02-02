# -*- coding: utf-8 -*-


import socketserver


class TcpServer(socketserver.BaseRequestHandler): # 通信循环
    def handle(self):
        print(self)
        print(self.request) # self.request 等效于 accept(),建立连接


if __name__ == "__main__":

    obj = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), TcpServer)
    print(obj.socket)
    obj.serve_forever()


#
