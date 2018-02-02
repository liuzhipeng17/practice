# -*- coding: utf-8 -*-

import logging
# 默认等级为warning, 只会显示高于warning的日志


logging.basicConfig(level=logging.DEBUG,
                    filename='example.log', # 有这个参数，说明日志是写到文件
                    # filemode='a'        # 写到文件的模式是：追加,这个默认设置是a
                    )

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical("critial message")
