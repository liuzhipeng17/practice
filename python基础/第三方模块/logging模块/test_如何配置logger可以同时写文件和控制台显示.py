# -*- coding: utf-8 -*-

import logging


def get_logger():
    # 设置logger等级
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置文件流和标准输出流stream
    fh = logging.FileHandler('logger2')
    sh = logging.StreamHandler()
    # 设置文件流的消息格式
    fm = logging.Formatter("%(asctime)s [%(lineno)s] %(message)s")
    fh.setFormatter(fm)
    logger.addHandler(fh)
    # 设置标准输出的消息格式
    sh.setFormatter(fm)
    logger.addHandler(sh)
    return logger

logger = get_logger()
logger.info('info message')
logger.debug('debug message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critial message')
