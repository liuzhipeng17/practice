# -*- coding: utf-8 -*-

# 工程内部各种函数的测试

import sys
import os
import time

ftp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ftp_path)

from ftp.src.client import Client
# from ftp.src.server import start_server

if __name__ == '__main__':
    c = Client()
    c.interactive()

