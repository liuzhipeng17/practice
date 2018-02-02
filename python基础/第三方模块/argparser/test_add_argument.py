# -*- coding: utf-8 -*-

# 这里是着重讲如何添加arguments
# ArgumentParser.add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])


import argparse

# 1 name or flages
    # #add_argument()方法必须知道一个可选参数，如- f或- foo，或一个位置参数，如文件名列表。因此，传递给add_arguments()的第一个参数必须是一系列标志，或者一个简单的参数名称。例如，可以创建一个可选参数:
    # #parser.add_argument('-f', '--foo') 可选参数，名字为foo
    # #parser.add_argument('bar') 位置参数名字为bar
# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('-f', '--foo')
# parser.add_argument('bar')
# print(parser.parse_args(['BAR']))
# # 上面的命令返回一个命名空间Namespace(bar='BAR', foo=None)
# print(parser.parse_args(['BAR', '--foo', 'FOO']))
# Namespace(bar='BAR', foo='FOO')

# 2 action
    ##ArgumentParser对象将命令行参数与动作关联起来。
    # 这些操作可以使用与它们相关联的命令行参数来做任何事情，
    # 尽管大多数操作只是将一个属性添加到parse_args()返回的对象中。
    # action关键字参数指定如何处理命令行参数

    # 有以下三种情况
    # action="store" 默认
    # action="store_const"， 将参数值由存储在const的值决定
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
# parser.add_argument('--foo', action='store_const', const=42)
s = parser.parse_args(['--foo'])
print(s)
# Namespace(foo=42)
    # action="store_true"， 参数在名称空间存储为True
    # action="store_false", 参数在名称空间存储为False