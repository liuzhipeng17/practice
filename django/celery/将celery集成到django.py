https://realpython.com/blog/python/asynchronous-tasks-with-djang

#step1 在django项目中，同名的app中新建celery.py

	from __future__ import absolute_import 
	import os 
	from celery import Celery 
	from django.conf import settings 

	# set the default Django settings module for the 'celery' program. 
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_celery.settings') 
	app = Celery('test_django_celery') 

	# Using a string here means the worker will not have to 
	# pickle the object when using Windows. 
	app.config_from_object('django.conf:settings') 

	app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) 

	@app.task(bind=True) 
	def debug_task(self): 
		print('Request: {0!r}'.format(self.request))
		

#step2 将celery.py 做成一个app; 其实就是使得django启动的时候，就加载celery应用。

"""
	简单说：将django和celery集成
	在settings.py旁边新建__init__.py，并将一下代码复制
	
"""
	from __future__ import absolute_import 

	# This will make sure the app is always imported when 
	# Django starts so that shared_task will use this app. 
	from .celery import app as celery_app
	

	
# step3 安装redis作为celery的中间件(worker)， 以及设置redis存储结果， 

"""
	celery是使用中间件在django项目和celery监控着之间传递消息， 我们使用redis来传递
	添加以下到settings.py中
	
	当然，安装redis 
	pip install redis==2.10.3
"""

# CELERY 
BROKER_URL = 'redis://localhost:6379' # 如果想要在其它数据库： 'redis://localhost:6379/3'   如果需要密码: redis://:2222@localhost:6379/3
CELERY_RESULT_BACKEND = 'redis://localhost:6379'     # 这里同样可以设置不同的数据库比如设置redis/4,  'redis://localhost:6379/4'
CELERY_ACCEPT_CONTENT = ['application/json'] 
CELERY_TASK_SERIALIZER = 'json' 
CELERY_RESULT_SERIALIZER = 'json' 
CELERY_TIMEZONE = 'Asia/Shanghai'



# step4 开启worker （先不要开启; 或者测试 celery -A 命令后，ctrl+c关闭）
	进入到manage.py 同级目录
	celery -A test_django_celery  worker  -l info
	
	# 其中test_django_celery 为celery app的名称， 要和app = Celery('test_django_celery') 里面一致
	# worker是一个执行任务角色，后面的loglevel=info记录日志类型默认是info,这个命令启动了一个worker,用来执行程序中add这个加法任务（task）。
	
"""

		[tasks]
		  . test_django_celery.celery.debug_task

		[2017-12-22 10:25:20,943: INFO/MainProcess] Connected to redis://localhost:6379//
		[2017-12-22 10:25:20,951: INFO/MainProcess] mingle: searching for neighbors
		[2017-12-22 10:25:21,971: INFO/MainProcess] mingle: all alone
		/opt/envlzp/local/lib/python2.7/site-packages/celery/fixups/django.py:202: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
		  warnings.warn('Using settings.DEBUG leads to a memory leak, never '

		[2017-12-22 10:25:21,980: WARNING/MainProcess] /opt/envlzp/local/lib/python2.7/site-packages/celery/fixups/django.py:202: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
		  warnings.warn('Using settings.DEBUG leads to a memory leak, never '

		[2017-12-22 10:25:21,987: INFO/MainProcess] celery@vagrant-ubuntu-trusty-64 ready.


"""
# step6 构建普通Python函数任务

from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task(name="sum_two_numbers") 
def add(x, y): 
	return x + y

	

# step7 新建一个view, 将add task压入消息队列（delay方法将task压入队列）

from .tasks import add

from django.http import HttpResponse


def testcelery(request):
    print 'hello'
    c = add.delay(1,2)
    return HttpResponse('hello')

	
# step8 设置url
	url(r'^test/$', testcelery)

	#打开浏览器输入网址： http://127.0.0.1:9000/test/


-# step9 打开redis， 查看消息队列(celery key)  
	redis-cli
	127.0.0.1:6379> keys *
	1) "celery"
	2) "_kombu.binding.celery"

	# 查看celery的类型
	127.0.0.1:6379> type "celery"
	list

	# 查看celery的值 （可以看出这是一个任务队列， 里面暂时只有一个任务； 因为没有开启worker, 所以这个任务没有执行，）
	127.0.0.1:6379> lrange celery 0 -1
	1) "{\"body\": \"W1sxLCAyXSwge30sIHsiY2hvcmQiOiBudWxsLCAiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbH1d\", \"headers\": {\"origin\": \"gen2803@vagrant-ubuntu-trusty-64\", \"root_id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"expires\": null, \"id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"kwargsrepr\": \"{}\", \"lang\": \"py\", \"retries\": 0, \"task\": \"sum_two_numbers\", \"group\": null, \"timelimit\": [null, null], \"parent_id\": null, \"argsrepr\": \"(1, 2)\", \"eta\": null}, \"content-type\": \"application/json\", \"properties\": {\"priority\": 0, \"body_encoding\": \"base64\", \"correlation_id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"reply_to\": \"7c1c68ce-01ae-3696-ae7d-fc30592d837c\", \"delivery_info\": {\"routing_key\": \"celery\", \"exchange\": \"\"}, \"delivery_mode\": 2, \"delivery_tag\": \"4e323344-2dd9-4efe-aa22-16d27bba0598\"}, \"content-encoding\": \"utf-8\"}"

	# 再次浏览网页:http://192.168.33.10:9000/test/
	
	# 查看redis celery , 可以看到多了一个任务
	127.0.0.1:6379> lrange celery 0 -1
	1) "{\"body\": \"W1sxLCAyXSwge30sIHsiY2hvcmQiOiBudWxsLCAiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbH1d\", \"headers\": {\"origin\": \"gen2803@vagrant-ubuntu-trusty-64\", \"root_id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"expires\": null, \"id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"kwargsrepr\": \"{}\", \"lang\": \"py\", \"retries\": 0, \"task\": \"sum_two_numbers\", \"group\": null, \"timelimit\": [null, null], \"parent_id\": null, \"argsrepr\": \"(1, 2)\", \"eta\": null}, \"content-type\": \"application/json\", \"properties\": {\"priority\": 0, \"body_encoding\": \"base64\", \"correlation_id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"reply_to\": \"7c1c68ce-01ae-3696-ae7d-fc30592d837c\", \"delivery_info\": {\"routing_key\": \"celery\", \"exchange\": \"\"}, \"delivery_mode\": 2, \"delivery_tag\": \"4e323344-2dd9-4efe-aa22-16d27bba0598\"}, \"content-encoding\": \"utf-8\"}"
	2) "{\"body\": \"W1sxLCAyXSwge30sIHsiY2hvcmQiOiBudWxsLCAiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbH1d\", \"headers\": {\"origin\": \"gen2505@vagrant-ubuntu-trusty-64\", \"root_id\": \"3a946360-f658-4cd5-b4d5-424aca49addf\", \"expires\": null, \"id\": \"3a946360-f658-4cd5-b4d5-424aca49addf\", \"kwargsrepr\": \"{}\", \"lang\": \"py\", \"retries\": 0, \"task\": \"sum_two_numbers\", \"group\": null, \"timelimit\": [null, null], \"parent_id\": null, \"argsrepr\": \"(1, 2)\", \"eta\": null}, \"content-type\": \"application/json\", \"properties\": {\"priority\": 0, \"body_encoding\": \"base64\", \"correlation_id\": \"3a946360-f658-4cd5-b4d5-424aca49addf\", \"reply_to\": \"01f98f1b-5975-31cc-b1e5-576b4e463c54\", \"delivery_info\": {\"routing_key\": \"celery\", \"exchange\": \"\"}, \"delivery_mode\": 2, \"delivery_tag\": \"863b0a08-aedb-4ffc-901a-2d9672cefb71\"}, \"content-encoding\": \"utf-8\"}"


	
- # step10 开启worker
	celery -A django_commitity  worker  -l info
	 
	 
	 -------------- celery@vagrant-ubuntu-trusty-64 v4.0.2 (latentcall)
	---- **** ----- 
	--- * ***  * -- Linux-3.13.0-137-generic-x86_64-with-Ubuntu-14.04-trusty 2018-01-23 13:56:01
	-- * - **** --- 
	- ** ---------- [config]
	- ** ---------- .> app:         django_commitity:0x7f6cfb88fed0
	- ** ---------- .> transport:   redis://localhost:6379//
	- ** ---------- .> results:     redis://localhost:6379/
	- *** --- * --- .> concurrency: 1 (prefork)
	-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
	--- ***** ----- 
	 -------------- [queues]
					.> celery           exchange=celery(direct) key=celery
					
	# 两个task
	[tasks]
	  . django_commitity.celery.debug_task
	  . sum_two_numbers

	[2018-01-23 13:56:01,706: INFO/MainProcess] Connected to redis://localhost:6379//
	[2018-01-23 13:56:01,721: INFO/MainProcess] mingle: searching for neighbors
	[2018-01-23 13:56:02,748: INFO/MainProcess] mingle: all alone
	[2018-01-23 13:56:02,773: WARNING/MainProcess] /home/vagrant/.virtualenvs/testenv/local/lib/python2.7/site-packages/celery/fixups/django.py:202: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
	  warnings.warn('Using settings.DEBUG leads to a memory leak, never '
	[2018-01-23 13:56:02,776: INFO/MainProcess] celery@vagrant-ubuntu-trusty-64 ready.
	
	# 从消息队列拿到任务task
	[2018-01-23 13:56:02,872: INFO/MainProcess] Received task: sum_two_numbers[3a946360-f658-4cd5-b4d5-424aca49addf]  
	[2018-01-23 13:56:02,874: INFO/MainProcess] Received task: sum_two_numbers[cd34e128-a047-4e65-9ea5-d3c97f91d9d0]  
	[2018-01-23 13:56:02,878: INFO/ForkPoolWorker-1] sum_two_numbers[3a946360-f658-4cd5-b4d5-424aca49addf]: the sum of 1 + 2 = 3
	[2018-01-23 13:56:02,885: INFO/ForkPoolWorker-1] Task sum_two_numbers[3a946360-f658-4cd5-b4d5-424aca49addf] succeeded in 0.00759203399957s: 'ok'
	[2018-01-23 13:56:02,903: INFO/ForkPoolWorker-1] sum_two_numbers[cd34e128-a047-4e65-9ea5-d3c97f91d9d0]: the sum of 1 + 2 = 3
	[2018-01-23 13:56:02,905: INFO/ForkPoolWorker-1] Task sum_two_numbers[cd34e128-a047-4e65-9ea5-d3c97f91d9d0] succeeded in 0.00125646800007s: 'ok'

# step11 打开redis 查看任务的结果

	127.0.0.1:6379> keys *
	1) "celery-task-meta-3a946360-f658-4cd5-b4d5-424aca49addf"
	2) "_kombu.binding.celery.pidbox"
	3) "celery-task-meta-cd34e128-a047-4e65-9ea5-d3c97f91d9d0"
	4) "_kombu.binding.celeryev"
	5) "_kombu.binding.celery"
	127.0.0.1:6379> 

	# 可以看到多了两个key， 分别为"celery-task-meta-3a946360-f658-4cd5-b4d5-424aca49addf"和"celery-task-meta-cd34e128-a047-4e65-9ea5-d3c97f91d9d0"
	127.0.0.1:6379> type "celery-task-meta-3a946360-f658-4cd5-b4d5-424aca49addf"
	string
	127.0.0.1:6379> get "celery-task-meta-3a946360-f658-4cd5-b4d5-424aca49addf"
	"{\"status\": \"SUCCESS\", \"traceback\": null, \"result\": \"ok\", \"task_id\": \"3a946360-f658-4cd5-b4d5-424aca49addf\", \"children\": []}"
	127.0.0.1:6379> type "celery-task-meta-cd34e128-a047-4e65-9ea5-d3c97f91d9d0"
	string
	127.0.0.1:6379> get "celery-task-meta-cd34e128-a047-4e65-9ea5-d3c97f91d9d0"
	"{\"status\": \"SUCCESS\", \"traceback\": null, \"result\": \"ok\", \"task_id\": \"cd34e128-a047-4e65-9ea5-d3c97f91d9d0\", \"children\": []}"
	127.0.0.1:6379> 

		
# 备注
此时会报错：
[2017-12-22 10:46:43,903: INFO/MainProcess] celery@vagrant-ubuntu-trusty-64 ready.
[2017-12-22 10:46:44,016: ERROR/MainProcess] Received unregistered task of type u'app01.tasks.add'.
The message has been ignored and discarded.

原因：应该是找不到tasks， 

	我没有验证的一个解决方法：在celery.py里面直接导入tasks应该可以， 或者直接在recely.py里定义tasks


经过验证的一个解决方法：

In your django settings you need to add each module that has a celery task to CELERY_IMPORTS

# 简单来说，就是在django.settigns.py里面添加一个配置项

CELERY_IMPORTS = (里面填写你有写celery task的模块)

CELERY_IMPORTS = (
    # 'reports.tasks',
    # 'some_app.some_module',
	'app01.tasks',
)

"""# 备注1 celery.py里面的各种配置说明
"""
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')
	设置这个环境变量是为了让 celery 命令能找到 Django 项目。这条语句必须出现在 Celery 实例创建之前。

	app = Celery('django_celery')
	这个 app 就是 Celery 

	app.config_from_object('django.conf:settings')
	可以将 settings 对象作为参数传入，但是更好的方式是使用字符串，因为当使用 Windows 系统或者 execv 时 celery worker 不需要序列化 settings 对象。

	app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
	为了重用 Django APP，通常是在单独的 tasks.py 模块中定义所有任务。
	Celery 会自动发现这些模块，加上这一句后，Celery 会自动发现 Django APP 中定义的任务，


# 备注2 celery是如何找到tasks的

要使celery找到相应的tasks有四种方法
1 在项目的celery中写tasks。即在djproj/djproj/celery.py中直接定义task

2 使用autodiscover 但是tasks必须定义在app目录下的名字为tasks.py的文件中，如：apps/app1/tasks.py 否则找不到 ，会报KeyError错误。

3 如果不使用autodiscover，可以在项目的celery中 import 相应的module，相当于在项目的celery中写了相应的task，如在celery.py中 import apps.app2.mytasks 

4 在settings.py中设置CELERY_IMPORTS = ('apps.app2.mytasks',) 写到module级 



