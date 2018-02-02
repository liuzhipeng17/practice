# -*- coding: utf-8 -*-

import socket
import argparse
import functools
import json
import struct
import hashlib
import os
import sys

from ..conf import settings


class Client(object):

    recv_buffer_size = 1024
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    encoding = 'utf-8'


    # server_address = ('127.0.0.1',8080)# 更好的方式是通过参数来获取，而不是通过配置文件或者写死

    def __init__(self):
        self.parse_arguments()
        self.connect()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="ftp client")
        parser.add_argument('-s', '--server', help='ftp server ip address')
        parser.add_argument('-P', '--port', type=int,
                            choices=range(1, 65535),
                            help='an integer for ftp server port')
        parser.add_argument('-u', '--username',help='user name')
        parser.add_argument('-p', '--password', help='user password')

        self.args = parser.parse_args()
        if not self.args.server:
            self.args = parser.parse_args('-s 127.0.0.1 -P 8080'.split())

        # print(self.args)

    def connect(self):
        # print('before connect')
        try:
            self.socket = socket.socket(self.address_family, self.socket_type)
            self.socket.connect((self.args.server, self.args.port))
            # print('connect successfully')
        except Exception:
            self.socket.close()

    def login(func): # 类中定义装饰器
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            flag = False
            if self.args.username:
                self.get_auth_result(self.args.username, self.args.password)
                flag = True
            else:
                retry_count = 0
                while retry_count < 3:
                    username = input('\033[1musername:\033[0m').strip()
                    password = input('\033[1mpassword:\033[0m').strip()
                    if self.get_auth_result(username, password):
                        flag = True
                        break
                    retry_count += 1

            if flag:
                func(self, *args, **kwargs) # 只有鉴权成功才会执行后面的操作
            else:
                exit(0)

        return wrapper

    def get_auth_result(self, username, password):
        tmp = ('%s%s'% (username, password)).encode('utf-8')
        password_md5 = self.calc_md5(tmp)
        data = {
            'action': 'auth',
            'username': username,
            'password': password_md5
        }
        self.send_request_test(data)
        try:
            auth_res_dict = self.recv_msg(convert_to_dict=True)
        except Exception:
            raise

        status_code = auth_res_dict.get('status_code')
        if status_code == 254:
            self.print(auth_res_dict.get('status_msg'))
            self.user = username
            self.cur_path = auth_res_dict.get('data').get('cur_path')
            return True
        elif status_code == 253:
            self.print(auth_res_dict.get('status_msg'))
            return False

    def _dir(self, cmd_list):
        cmd_str = ' '.join(map(str, cmd_list))
        data = {'action': 'listdir',
                'username': self.user,
                'cmd': cmd_str,
                }
        self.send_request_test(data)
        try:
            self.print(self.recv_msg().decode('gbk'))
        except Exception:
            raise

    def _cd(self, cmd_list):
        cmd_str = ' '.join(map(str, cmd_list))
        data = {'action': 'change_dir',
                     'username': self.user,
                     'cmd': cmd_str,
                     }
        self.send_request_test(data)
        try:
            result = self.recv_msg(convert_to_dict=True)
        except Exception:
            raise
        self.cur_path = result.get('data').get('cur_path')
        self.print(result.get('status_msg'))# 应该打印消息

    def _pwd(self, cmd_list):
        cmd_str = ' '.join(map(str, cmd_list))
        data = {'action': 'pwd',
                'username': self.user,
                'cmd': cmd_str,
                }
        self.send_request_test(data)
        try:
            result= self.recv_msg(convert_to_dict=True)
        except Exception:
            raise OSError('dir recv error')  # 传递给上层

        self.print(result.get('data').get('pwd'))

    def _get(self, cmd_list):
        cmd_str = ' '.join(map(str, cmd_list))
        if len(cmd_list) != 2:
            self.print('invalid get command, please type help for detail')
            return

        filename = cmd_list[-1]
        basename = os.path.basename(filename)
        local_filename = os.path.join(settings.USER_DOWNLOAD_BASE_DIR,
                                      self.user,
                                      basename,)
        data_dict = {'action': 'get',
                     'username': self.user,
                     'cmd': cmd_str,
                     'basename': basename,
                     'filename': filename, # 不能缺少
                     'local_filename': local_filename,
                     }
        if os.path.exists(local_filename):
            self.print('%s has exist' % local_filename)
            while True:
                choice = input('\033[;34m1: overlay it or 2:save as new name: \033[0m').strip()
                if choice == '2':
                    while True:
                        rename = input("\033[;34msave as: \033[0m").strip()
                        local_filename = os.path.join(os.path.dirname(local_filename),rename)
                        if not rename:
                            self.print('the name is not allowed to be empty')
                        elif os.path.exists(local_filename):
                            self.print('%s has exist' % local_filename)
                        else:
                            data_dict.update({'local_filename': local_filename})
                            break
                    break
                elif choice == '1':
                    os.remove(local_filename)
                    break
                else:
                    self.print('invalid choice, please select again')

        self.get_file(data_dict)

    def get_file(self, data_dict):
        local_filename = data_dict.get('local_filename')
        # part1 send request
        self.send_request_test(data_dict)
        # part2 recv response
        response_dict = self.recv_msg(convert_to_dict=True)
        status_code = response_dict.get('status_code')
        if status_code == 256:
            self.print(response_dict.get('status_msg'))
            # print('\033[;34m%s\033[0m'%response_dict.get('status_msg'))
            return
        if status_code == 265:
            self.print(response_dict.get('status_msg'))
            # print('\033[;34m%s\033[0m' % response_dict.get('status_msg'))
            f = open(local_filename, 'wb')
            f.close()
            return
        file_size = response_dict.get('data').get('file_size')
        # part3 send ready signal
        self.socket.send(b'ready')
        # part4 receive file
        f = open(local_filename, 'wb')
        md5_obj = hashlib.sha256()
        recv_size = 0
        while recv_size < file_size:
            try:
                line_bytes = self.recv_msg()
                f.write(line_bytes)
                recv_size += len(line_bytes)
                md5_obj.update(line_bytes)
                cur_percent = recv_size / file_size * 100
                sys.stdout.write("\r\033[;34mdownload%10.4s%s\033[0m" % (cur_percent, '%'))
                sys.stdout.flush()
            except:
                f.close()
                raise
        f.close()
        print()
        # part4 verify the consistency of file
        md5_local_file = md5_obj.hexdigest()
        md5_server_file = self.recv_msg().decode('utf-8') # 服务端最后还发了一个md5值过来
        if md5_local_file == md5_server_file:
            self.print('verify consistency pass')

    def _put(self, cmd_list):
        # upload file to server current path
        cmd_str = ' '.join(map(str, cmd_list))
        # check cmd format
        if len(cmd_list) != 2:
            self.print('invalid get command, please type help for detail')
            return
        # check whether local file is exist or not
        local_filename = cmd_list[-1]
        # not support relative path
        if not os.path.isfile(local_filename):
            self.print('%s is not exist' % local_filename)
            return
        
        # file exists, and send file_size and md5
        file_size = os.path.getsize(local_filename)
        basename = os.path.basename(local_filename)
        data = {'action': 'put',
                'username': self.user,
                'cmd': cmd_str,
                'basename': basename,
                'file_size': file_size,
                }
        # send request
        self.send_request_test(data)
        # receive response from server
        response = self.recv_msg(convert_to_dict=True)
        status_code = response.get('status_code')
        # self.print(status_code)
        if status_code == 256:
            self.put_with_not_continue(local_filename, file_size)
        elif status_code == 262: # server has exist the same file
            self.put_with_continue()

    def put_with_not_continue(self, filename, file_size):
        if not file_size:
            self.print("put empty file is allowed, in the case of server don't has same-name file")
            return
        assert self.socket.recv(5) == b'ready'
        m = hashlib.sha256()
        send_size = 0
        with open(filename, 'rb') as f:
            for line in f:
                m.update(line)
                head_dict = {'data_size': len(line)}
                self.send_cmd(head_dict, line)
                send_size += len(line)
                cur_percent = send_size / file_size * 100
                sys.stdout.write("\r\033[;34mupload%10.4s%s\033[0m" % (cur_percent, '%'))
                sys.stdout.flush()
        print()
        # receive md5 of server file
        md5_from_server = self.recv_msg().decode('utf-8')
        if md5_from_server == m.hexdigest():
            self.print("verify consistency successfully")
        else:
            self.print("verify consistency fail")

    def put_with_continue(self, filename, file_size):
        if file_size == 0:
            self.print("permit putting empty file, in case of overwriting server the same-name file")
            return

        data = self.recv_msg(convert_to_dict=True)
        server_file_size = data.get('data').get('file_size')
        if file_size <= server_file_size:
            self.print("permitted putting same-name file unless continue situation")
            return

        # 暂时不考虑同名但不是续传的情况
        size = 0
        m = hashlib.sha256()
        f = open(filename, 'rb')
        while size < file_size:
            for line in f:
                m.update(line)
                length = len(line)
                size += length
                if size < server_file_size:
                    pass
                else:
                    head_dict = {'data_size': length}
                    self.send_cmd(head_dict, line)
                    cur_percent = size / file_size * 100
                    sys.stdout.write("\r\033[;34mupload%10.4s%s\033[0m" % (cur_percent, '%'))
                    sys.stdout.flush()

        f.close()
        print()
        md5_from_server = self.recv_msg().decode('utf-8')
        if md5_from_server == m.hexdigest():
            self.print("verify consistency successfully")
        else:
            self.print("verify consistency fail")


    def send_cmd(self, head_dict, data_bytes):
        # 首先发送报头长度
        head_str = json.dumps(head_dict)
        head_bytes = head_str.encode(self.encoding)
        head_len_int = len(head_bytes)
        head_len_bytes = struct.pack('i', head_len_int)
        self.socket.send(head_len_bytes)

        # 接着发送报头
        self.socket.send(head_bytes)

        # 最后发送data
        self.socket.send(data_bytes)

    def send_request_test(self, data):
        data_bytes = json.dumps(data).encode('utf-8')
        head_dict = {'data_size': len(data_bytes)}

        # 首先发送报头长度
        head_str = json.dumps(head_dict)
        head_bytes = head_str.encode(self.encoding)
        head_len_int = len(head_bytes)
        head_len_bytes = struct.pack('i', head_len_int)
        self.socket.send(head_len_bytes)

        # 接着发送报头
        self.socket.send(head_bytes)

        # 最后发送data
        self.socket.send(data_bytes)

    def recv_msg(self, convert_to_dict=False):
        # 先接收报头长度
        head_len_bytes = self.socket.recv(4)
        if not head_len_bytes:
            raise
        head_len_int = struct.unpack('i', head_len_bytes)[0]

        # 再接收报头
        head_bytes = self.socket.recv(head_len_int)
        if not head_bytes:
            raise
        head_str = head_bytes.decode(self.encoding)
        head_dict = json.loads(head_str)
        data_size = head_dict["data_size"]

        # 最后接收数据
        recv_data = b''
        recv_size = 0
        while recv_size < data_size:
            data = self.socket.recv(self.recv_buffer_size)
            if not data:
                raise
            recv_size += len(data)
            recv_data += data
        if not convert_to_dict:
            return recv_data
        else:
            response = json.loads(recv_data.decode('utf-8'))
            return response

    def _help(self, *args, **kwargs):
        print("""
        get filename    # download file from FTP server
        put filename    # upload file to FTP server
        dir             # dir files in current dir on FTP server
        pwd             # check current path on server
        cd path         # change directory , same usage as linux cd command
        """)

    # def get_file_md5(self, filename):
    #     g = ReadFile(filename)
    #     m = hashlib.sha256()
    #     for line in g:
    #         m.update(line)
    #     return m.hexdigest()

    def calc_md5(self, data_bytes):
        m = hashlib.sha256()
        m.update(data_bytes)
        return m.hexdigest()

    @login
    def interactive(self):
        while True:
            # print(self.cur_path)
            cmd = input('\033[1m%s@%s%s:\033[0m' % (self.user, self.args.server,self.cur_path)).strip()
            cmd = cmd.split()
            # print(cmd)
            if not cmd:
                continue
            elif hasattr(self, '_%s'% cmd[0]):
                func = getattr(self, '_%s'% cmd[0])
                func(cmd)# 传入的cmd是一个列表
            else:
                self.print("invalid command, type 'help' for detail information" )

    def print(self, msg):
        print('\033[;34m%s\033[0m'% msg)


# class ReadFile(object):
#     def __init__(self, data_path):
#         self.data_path = data_path
#
#     def __iter__(self):
#         with open(self.data_path, 'rb') as f:
#             for line in f:
#                 yield line


# if __name__ == "__main__":
#     c = Client()
#     c.cc()
