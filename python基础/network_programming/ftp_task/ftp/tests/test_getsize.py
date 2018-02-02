import os

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'example.ini')
print(os.path.getsize(filename)) # 单位是bytes