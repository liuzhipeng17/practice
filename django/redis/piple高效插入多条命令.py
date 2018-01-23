# -*- coding: utf-8 -*-
import redis


host = "127.0.0.1"
port = 7379

# 将三条redis命令一次搞定，只需要和redis服务器一次通信即可，提供效率
pool = redis.ConnectionPool(host=host, port=port)
r = redis.StrictRedis(connection_pool=pool)
p = r.pipeline()        #创建一个管道
p.set('hello','redis')
p.sadd('faz','baz')
p.incr('num')
p.execute()        # 执行管道内命令
# 结果[True, 1, 1]