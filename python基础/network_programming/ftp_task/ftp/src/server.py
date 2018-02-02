# -*- coding: utf-8 -*-


import socketserver
import json
import struct
import subprocess
import os.path
import re
import hashlib

import configparser

from ..conf import settings
# from .readfile import ReadFile

STATUS_CODE = settings.STATUS_CODE


class TcpServer(socketserver.BaseRequestHandler): # 通信循环
    encoding = settings.ENCODING
    max_recv_buffer_size = settings.MAX_BUFFER_SIZE
    user_db = settings.USER_DB_PATH
    user_base_dir = settings.USER_BASE_PATH
    base_dir = settings.BASE_DIR

    def handle(self):  # 一个连接的通信循环
        print(self.request)
        while True:
            try:
                recv_cmd = self._recv_msg()
            except Exception:
                print('client closed')
                break
            # 发送过来的消息必须先包装成dict, 不然这里报错
            recv_cmd = json.loads(recv_cmd.decode(self.encoding))
            if hasattr(self, '_%s' % recv_cmd['action']):
                func = getattr(self, '_%s' % recv_cmd['action'])
                func(recv_cmd) # 记住这里必须要包含send_response
            else:
                print('%s is currently not supported' % recv_cmd['action'])
                self._send_500(recv_cmd) # invalid command

    def _auth(self, data):
        auth_info_dict = data # data was client user info
        username = auth_info_dict['username']
        password = auth_info_dict['password']
        config = configparser.ConfigParser()
        config.read(self.user_db)
        if username in config and password == config[username]['password']:
            self.cur_dir = os.path.join(self.user_base_dir, username)
            self.home_dir = os.path.join(self.user_base_dir, username)
            auth_result = {'cur_path': self.get_relative_path(self.cur_dir)}
            # print(self.get_relative_path(self.cur_dir))
            self._send_response_test(254, auth_result)
        else:
            self._send_response_test(253)

    def _listdir(self, data):
        cmd = data['cmd']
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                cwd=self.cur_dir)
        (out, err) = proc.communicate()
        data_bytes = out + err
        head_dict = {'data_size': len(data_bytes)}
        self._send_response(head_dict, data_bytes)

    def _change_dir(self, data):
        status_code = 0
        response = {}
        cmd = data['cmd']
        cmd_list = cmd.split()
        length = len(cmd_list)
        if length == 2:
            real_path = os.path.abspath(os.path.join(self.cur_dir, cmd_list[-1]))
            if real_path.startswith(self.home_dir) and os.path.isdir(real_path): # accessible
                status_code = 260 # "path changed"
                self.cur_dir = real_path
            else:
                status_code = 266 # "Path access permitted or Path not exist"
        elif length == 1:
            self.cur_dir = self.home_dir
            status_code = 260 # "path changed"
        else:
            status_code = 251 # "Invalid cmd "

        response.update({'cur_path': self.get_relative_path(self.cur_dir)})
        self._send_response_test(status_code, response)

    def _pwd(self, data):
        response = {}
        cmd_list = data['cmd'].split()
        if len(cmd_list) > 1:
            status_code = 267
            response = {'pwd': settings.STATUS_CODE.get(status_code)}
        else:
            status_code = 268
            response = {'pwd': self.get_relative_path(self.cur_dir)}

        self._send_response_test(status_code, response)

    def _get(self, data):
        response = {}
        filename = data.get('filename')
        real_path = os.path.abspath(os.path.join(self.cur_dir,
                                                 filename
                                                 ))
        file_size = os.path.getsize(real_path)
        if not os.path.isfile(real_path):
            self._send_response_test(256)
            return
        if file_size == 0:
            self._send_response_test(265)
        else:
            self._send_response_test(257,{'file_size': file_size})
            assert self.request.recv(5) == b'ready', "recv error"
            m = hashlib.sha256()
            with open(real_path, 'rb') as f:
                for line in f:
                    m.update(line)
                    head_dict = {"data_size": len(line)}
                    self._send_response(head_dict, line)

            # 发送 md5
            md5_bytes = m.hexdigest().encode('utf-8')
            head_dict = {"data_size": len(md5_bytes)}
            self._send_response(head_dict, md5_bytes)

    def _put(self, data):
        response = {}
        basename = data.get('basename')
        filename = os.path.join(self.cur_dir, basename)
        file_size = data.get('file_size')
        if os.path.exists(filename):
            self._send_response_test(262)
            self.put_with_continue(filename, file_size)
        else:
            self._send_response_test(256)
            self.put_with_not_continue(filename, file_size)

    def put_with_not_continue(self, filename, file_size):
        f = open(filename, 'wb')  # wb模式，存在则清除内容，不存在则创建
        if file_size == 0:  # 增加传递空文件
            f.close()
            return

        self.request.send(b'ready')
        # receive file
        m = hashlib.sha256()
        recv_size = 0
        while recv_size < file_size:
            try:
                line = self._recv_msg()
                f.write(line)
                recv_size += len(line)
                m.update(line)
            except:
                f.close()
                raise

        f.close() # note no less
        # send md5
        md5 = m.hexdigest().encode('utf-8')
        head_dict = {'data_size': len(md5)}
        self._send_response(head_dict, md5)

    def put_with_continue(self,filename, file_size):

        if file_size == 0:
            return
        server_file_size = os.path.getsize(filename)
        if server_file_size >= file_size:
            return

        data = {'file_size': server_file_size}
        self._send_response_test(270, data)
        f = open(filename, 'ab')
        # receive file
        m = hashlib.sha256()
        recv_size = server_file_size
        f.seek(recv_size, 0)
        while recv_size < file_size:
            try:
                line = self._recv_msg()
                f.write(line)
                recv_size += len(line)
                m.update(line)
            except:
                f.close()
                raise

        f.close() # note no less
        # send md5
        md5 = m.hexdigest().encode('utf-8')
        head_dict = {'data_size': len(md5)}
        self._send_response(head_dict, md5)







        data = self._recv_msg().decode('utf-8')
        data_dict = json.loads(data)
        md5_from_client = data_dict.get('md5')

        m = hashlib.sha256()
        # with

        response.update({'md5': m.hexdigest()})

        self._send_response_test(262, response)

    def get_relative_path(self, real_path):
        pattern = self.base_dir.replace('\\','\\\\')
        relative_path = re.sub("^%s" % pattern, '', real_path)
        return relative_path

    def _send_response(self, head_dict, data_bytes):
        # 首先发送报头长度
        head_str = json.dumps(head_dict)
        head_bytes = head_str.encode(self.encoding)
        head_len_int = len(head_bytes)
        head_len_bytes = struct.pack('i', head_len_int)
        self.request.send(head_len_bytes)

        # 接着发送报头
        self.request.send(head_bytes)

        # 最后发送data
        self.request.send(data_bytes)
        return

    def _send_response_test(self, status_code, data=None):
        # data最好为字符串或字典
        response = {"status_code": status_code,
                    "status_msg": STATUS_CODE[status_code],
                    }

        if data:
            response.update({"data": data})

        # 制作报头
        response_bytes = json.dumps(response).encode(self.encoding)
        head_dict = {"data_size": len(response_bytes)}

        # 首先发送报头长度
        head_str = json.dumps(head_dict)
        head_bytes = head_str.encode(self.encoding)
        head_len_int = len(head_bytes)
        head_len_bytes = struct.pack('i', head_len_int)
        self.request.send(head_len_bytes)

        # 接着发送报头
        self.request.send(head_bytes)

        # 最后发送data
        self.request.send(response_bytes)
        return

    def _recv_msg(self):
        # 先接收报头长度
        head_len_bytes = self.request.recv(4)
        if not head_len_bytes:
            # print('client closed') # linux处理
            raise
        head_len_int = struct.unpack('i', head_len_bytes)[0]

        # 再接收报头
        head_bytes = self.request.recv(head_len_int)
        if not head_bytes:
            # print('client closed') # linux处理
            raise
        head_str = head_bytes.decode(self.encoding)
        head_dict = json.loads(head_str)
        data_size = head_dict["data_size"]

        # 最后接收数据
        recv_data = b''
        recv_size = 0
        while recv_size < data_size:
            data = self.request.recv(self.max_recv_buffer_size)
            if not data:
                # print('client closed') # linux处理
                raise
            recv_size += len(data)
            recv_data += data

        return recv_data

    def _send_500(self, response):
        response.update({'status_code': '500', 'status_msg': 'invalid command'})
        response_bytes = json.dumps(response).encode(self.encoding)
        head_dict = {'data_size': len(response_bytes)}
        self._send_response(head_dict, response_bytes)
        return


def start():
    obj = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), TcpServer)
    obj.serve_forever()
    ## 开辟了多个线程（多个服务员）ThreadingTcpServer
    # 每个服务员，循环利用（多次循环链接） obj.server_forserver()
    # 每个链接里面，循环提供服务（TcpServer)

# if __name__ == '__main__':
#     start_server()