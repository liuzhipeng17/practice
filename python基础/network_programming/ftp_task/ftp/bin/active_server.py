import sys
import os

ftp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ftp_path)

from ftp.src.server import start

if __name__ == '__main__':
    start()