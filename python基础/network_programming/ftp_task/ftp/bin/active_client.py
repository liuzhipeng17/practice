# -*- coding: utf-8 -*-

import sys
import os


ftp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ftp_path)

from ftp.src.client import Client
# from ftp.src.server import start_server

if __name__ == '__main__':
    c = Client()
    c.interactive()

