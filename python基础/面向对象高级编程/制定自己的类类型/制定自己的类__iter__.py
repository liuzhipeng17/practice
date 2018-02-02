# -*- coding: utf-8 -*-


class ReadStaffInfo(object):
    def __init__(self, data_path):
        print('exec __init__')
        self.data_path = data_path

    def __iter__(self):
        print('exec __iter__')
        with open(self.data_path) as f:
            for line in f:
                yield line.strip(',').rstrip('\n')
        # 调用iter就会得到一个迭代器（用yield)


r = ReadStaffInfo('a1.txt')
for i in r:
    pass

# 输出结果如下：
# exec __init__
# exec __iter__
