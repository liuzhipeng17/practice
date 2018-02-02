# -*- coding: utf-8 -*-

import logging
# 默认等级为warning, 只会显示高于warning的日志


logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)-10s%(asctime)-22s%(name)-6s[%(lineno)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    # filename='logger', # 有这个参数，说明日志是写到文件
                    # filemode='a'        # 写到文件的模式是：追加
                    )



logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical("critial message")

# filename  指定了文件Handler记录日志，而不再是显示到控制台
# filemode  如果指定了filename参数，可以选择文件打开模式：默认是a；
# format   指定写入文件或者控制台的字符串格式
# datefmt  指定datatime格式化
# level    指定logger的级别
# stream   该参数不能喝filename同时存在，如果同时设置，stream被忽略

#format的设置格式：
#asctime    %{asctime}s
#filename   %{filename}s  # 这个和上面filename不一样，这个是.py的文件名
#funcname   %{funcname}s  # 函数名字
#levelname  %{levelname}s #日记级别
#threadName %{threadName}s # 线程名字
#lineno     %{lineno}s 行号
#name      %{name}s  logger的名字这里是root





