import os.path

path = r'F:\oldboy\network_programming\ftp_task\ftp\dir\home\lzp\ff'

print(os.path.getsize(path))


filename = r'\\rr\\d.txt'
print(os.path.basename(filename))
print(filename.split(os.sep)[-1] )