# -*- coding: utf-8 -*-

# os.abspath(path)返回path的绝对路径， 而且是规范化的路径，等效于
# os.path.normpath(os.path.join(os.getcwd(),path)

import os

path = os.path.join(__file__,
                    '..',
                    '..'
                    )
print(path)
print(os.path.realpath(path))
print(os.path.abspath(path))
#F:\oldboy\常用模块\os模块\os_path模块