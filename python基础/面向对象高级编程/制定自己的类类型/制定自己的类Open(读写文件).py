# -*- coding: utf-8 -*-

# 自己定义一个类，读写内容，要求将当期时间写进去；其他属性还是继承open来

from time import localtime, strftime, sleep


class Open(object):
    def __init__(self, file_path, mode='r'):
        # print 'exec __init__'
        self.f = open(file_path, mode=mode)

    def write(self, line):
        print('exec write')
        local_tuple = localtime()
        time_format = '%Y-%m-%d %H:%M:%S'
        time_str = strftime(time_format, local_tuple)
        self.f.write('%s %s\n' % (time_str, line))

    def __getattr__(self, item):
        print('exec __getattr__')
        return getattr(self.f, item)
        # getattr中的self.f是一个对象

    # 析构函数，当代码执行完或者 del 实例化对象时，会触发__del__执行
    # 该函数的作用：清理资源（关闭文件，浏览器，关闭数据库连接等）
    def __del__(self):
        print('exec __del__')
        self.f.close()

    # 将对象返回，就是返回self, 不要返回self.f；不然执行write，会调用真正的write
    def __enter__(self):
        print('exec __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭文件，
        self.f.close()
        # return True #可以增加忽略异常
with Open('a1.txt', 'a+') as f:
    f.write('liuzhipeng is working')
    sleep(5)
    f.write('liuzhipeng is having a set')
    f.seek(0)
    print(f.read())

print("end")
