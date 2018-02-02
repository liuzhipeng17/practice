
# -*- coding: utf-8 -*-

import logging


FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger("tcpServer")
logger.warning('Protocol problem: %s', 'connection reset',extra=d)

# 这种方式是非常不安全的，
# 2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset