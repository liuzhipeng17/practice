import argparse


parser = argparse.ArgumentParser(description="ftp client")
parser.add_argument('-s', '--server', help='ftp server ip address')
parser.add_argument('-P', '--port', type=int,
                    choices=range(1, 65535),
                    help='an integer for ftp server port')
parser.add_argument('-u', '--username', help='user name')
parser.add_argument('-p', '--password', help='user password')
# args = parser.parse_args()
args = parser.parse_args('-s 127.0.0.1 -P 8080 -p 123'.split())
print(args)
# Namespace(password='123', port=8080, server='127.0.0.1', username='lzp')
print(args.password)
print(args.username)