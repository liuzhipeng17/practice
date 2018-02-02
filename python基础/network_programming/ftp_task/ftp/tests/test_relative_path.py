import re
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_relative_path(real_path, BASE_DIR):
    # pattern = r'F:\\oldboy\\network_programming\\ftp_task\\ftp'
    pattern = BASE_DIR.replace("\\","\\\\")
    relative_path = re.sub('^%s' % pattern, '', real_path)
    return relative_path

print(BASE_DIR)
real_path = os.path.join(BASE_DIR,
                         'dir',
                         'home')
print(real_path)
print(get_relative_path(real_path, BASE_DIR))