import sys, time

for i in range(5):
    # sys.stdout.write('\r')
    sys.stdout.write('\r*********{0}/5'.format(i + 1))
    # sys.stdout.flush()
    time.sleep(0.1)
print()
import os.path
filename = r'F:\oldboy\network_programming\ftp_task\ftp\dir\home\lzp\ff'
print(os.path.getsize(filename))
filename = r'F:\oldboy\network_programming\ftp_task\ftp\dir\downloads\Lzp\ff'
print(os.path.getsize(filename))