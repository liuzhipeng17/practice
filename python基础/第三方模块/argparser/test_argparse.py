# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Ftp client')
# 添加位置参数(不用带-）
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# integers: 说明这个参数名字是integers，可以通过解析后获取
# metavar
# ype=int 默认参数类型为string，可以通过type设置类型，参数类型不一样会报类型错误
# help 是对这个参数的说明
# nargs

# 添加可选参数
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')


# dest通过解析后，其值保存在args.accumulate(有dest),没有dest保存在integers
# action

args = parser.parse_args()
#parse_args()返回一个对象，该对象拥有两个属性：integers，accumulate
#integers是列表，元素为整形
#accumulate为函数名，如果命令行指明--sum，则为sum(),否则为max()
print(args.integers)
print(args.accumulate)
print(args.accumulate(args.integers))


# F:\oldboy\network_programming\ftp_task\tests
# λ python test_argparse.py 1 2 3
# [1, 2, 3]
# <built-in function max>
# 3
#
# F:\oldboy\network_programming\ftp_task\tests
# λ python test_argparse.py --sum 1 2 3 4
# [1, 2, 3, 4]
# <built-in function sum>
# 10

# ArgumentParser通过parse_args()方法解析参数。
# 这将检查命令行，将每个参数转换为适当的类型，然后调用适当的操作。
# 在大多数情况下，这意味着一个简单的名称空间对象将从命令行解析属性中建立起来:
# parser.parse_args(['--sum', '7', '-1', '42']) # 列表传递参数
# Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])