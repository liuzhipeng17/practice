"""
安装celery， 4.0以后不支持windows，所以最好为 pip install celery==3.1.25， linux除外

"""

"""
celery 异步处理需要传递消息和处理任务和存储结果， 采用经典的生产-消费者模式

celery包含三个结构：broker（消息队列）、workers（消费者：处理任务）、backend（存储结果）

应用场景：web前端发送一个请求， 只需要将请求要处理的任务丢给borker, 由空闲的worker去执行任务，处理的结果会存储在backend中。

celery现在已经统一为一个版本，不要再用django-celery

broker:推荐使用RabbitMQ, redis(这两个都可以在生成环境上使用）



我的环境：
	pip install celery==3.1.25
	pip install redis

"""

#1 新建一个tasks.py

from celery import Celery
import celeconfig


app = Celery('tasks')
app.config_from_object('celeconfig')

@app.task
def add(x, y):
    return x + y

	
#2 新建celeconfig.py

BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True


#3 切换到tasks.py的上一级目录（一定）--不是在python环境，是linux命令输入
	celery -A tasks worker --loglevel=info

	"""
		不要ctrl+c关掉
		
		[2017-12-22 09:46:30,055: INFO/MainProcess] Received task: tasks.add[df36f165-5ec8-4095-b22c-6c29656d6aa9]  
		[2017-12-22 09:46:30,057: INFO/MainProcess] Received task: tasks.add[8d8e6d9e-f891-46c5-86e7-694cd7f98fb8]  
		[2017-12-22 09:46:30,067: INFO/MainProcess] Received task: tasks.add[4d3d90cb-baf2-40ec-8750-e3c925b1bc4b]  
		[2017-12-22 09:46:30,070: INFO/MainProcess] Received task: tasks.add[184832a2-f790-4b15-b23c-9d32ed08add6]  
		[2017-12-22 09:46:30,076: INFO/PoolWorker-1] Task tasks.add[df36f165-5ec8-4095-b22c-6c29656d6aa9] succeeded in 0.0172910700057s: 3
		[2017-12-22 09:46:30,078: INFO/MainProcess] Received task: tasks.add[6bdccafa-9ac0-4c55-86e5-9c8bb67d0fc5]  
		[2017-12-22 09:46:30,087: INFO/PoolWorker-1] Task tasks.add[8d8e6d9e-f891-46c5-86e7-694cd7f98fb8] succeeded in 0.00250590100768s: 3
		[2017-12-22 09:46:30,091: INFO/PoolWorker-1] Task tasks.add[4d3d90cb-baf2-40ec-8750-e3c925b1bc4b] succeeded in 0.00107305000711s: 3
		[2017-12-22 09:46:30,100: INFO/PoolWorker-1] Task tasks.add[184832a2-f790-4b15-b23c-9d32ed08add6] succeeded in 0.000554775993805s: 5
		[2017-12-22 09:46:30,102: INFO/PoolWorker-1] Task tasks.add[6bdccafa-9ac0-4c55-86e5-9c8bb67d0fc5] succeeded in 0.000582449996728s: 5
		[2017-12-22 09:48:59,603: INFO/MainProcess] Received task: tasks.add[613a813f-3b95-49fd-aab6-07b46a61cbd5]  
		[2017-12-22 09:48:59,606: INFO/PoolWorker-1] Task tasks.add[613a813f-3b95-49fd-aab6-07b46a61cbd5] succeeded in 0.000856857994222s: 4
	"""

	
#4 打开另外一个终端，进入tasks.py的同级目录， 进入python console环境
"""
>>>from tasks import add
>>>c = add.delay(3,4)
>>> c.get(timeout=1)
"""

"""
	执行add.delay(3,4)
	会在前面一个终端，看到：Task tasks.add[e3be5b2b-3549-4567-9757-ff9e72d5bd94] succeeded in 0.000766809011111s: 7
	c.get(timeout=1), 一定要timeout，不然就是同步不是异步了
"""







