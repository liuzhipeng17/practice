# -*- coding: utf-8 -*-

"""
使用管道高性能插入数据
"""

# 如果使用下面的代码，导入300000条数据，速度回非常慢。
# import redis
# pool = redis.ConnectionPool(host=host, port=port)
# client = redis.StrictRedis(connection_pool=pool)
#
# for i in range(10000):
#     for j in range(30):
#         client.lpush(IDLE_TASKS, json.dumps(args))



pool = redis.ConnectionPool(host=host, port=port)
client = redis.StrictRedis(connection_pool=pool)

p = client.pipeline()
for i in range(10000):
    for j in range(30):
        p.lpush(IDLE_TASKS, json.dumps(args))
p.execute()


# 使用了管道，Redis 会将命令暂时存储，当遇到 execute() 时才会执行，
# 所以上面代码只需要和 Redis 服务器通信一次即可将数据全部插入

# 理解：管道为git的本地暂存区， 服务器是本地仓库。
# 先将命令暂存到缓存区，然后执行execute就会将缓存区的所有命令提交给服务器


