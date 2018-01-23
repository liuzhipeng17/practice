# step1 安装redis模块
	pip install redis
	
# step2 python调用redis

	# -*- coding: utf-8 -*-
	import redis

	#from django.conf import settings


	class CustomRedis(object):
		def __init__(self,host,port,db):
			self.host = host
			self.port = port
			self.db = db
			pool = redis.ConnectionPool(host=self.host,port=self.port,db=self.db)
			self.connect = redis.Redis(connection_pool=pool)

		def set_key(self,key,value,expired=None):
			return self.connect.set(key, value, ex=expired) if expired else self.connect.set(key, value)

		def get_key(self,key):
			return self.connect.get(key)

		def list_keys(self):
			return self.connect.keys()


	if __name__ =='__main__':
		import pdb
		pdb.set_trace()
		redisDB = CustomRedis('127.0.0.1',6379, 1) 
		#redisDB = CustomRedis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB)
		redisDB.set_key('liu', 18, 3600)
		
		
# step3 将host, port, db设置到django settings里面

	REDIS_HOST='127.0.0.1'
	REDIS_PORT=6379
	REDIS_DB=0
		
# redis 怎么切换db
	redis-cli
	
	select 1 # 切换到db=1的redis