# -*- coding: utf-8 -*-

import logging
"""
创建一个Logger,
创建一个handler(可以console， 也可以是file)
设置handler的format,level
添加设置好的handler到Logger
可以同时添加多个handler(比如StreamHandler，FileHandler)
"""

# 创建一个logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

#创建一个console handler以及设置它的日志级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 设置format
formatter = logging.Formatter("%(levelname)-10s%(asctime)-25s%(name)-15s[%(lineno)s] %(message)s")

# 将设置的format添加到ch
ch.setFormatter(formatter)

# 将设置的hander添加到logger
logger.addHandler(ch)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
