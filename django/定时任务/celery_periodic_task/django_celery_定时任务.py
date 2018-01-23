# celery部署定时任务

"""refer to http://celery.readthedocs.io/en/latest/userguide/periodic-tasks.html
"""

# step1 在settings.py里面设置
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {   
				# Executes every Monday morning at 7:30 A.M   
				'add-every-monday-morning': {       
						'task': 'member.tasks.add',    
						'schedule': crontab(hour=7, minute=30, day_of_week=1),        
						'args': (16, 16),    
				},
}

# step2 在crontab里面可以设置的参数

"""class celery.schedules.crontab(minute=u'*', hour=u'*', day_of_week=u'*', day_of_month=u'*', month_of_year=u'*', **kwargs)"""


# step3 如何设置crontab的时间参数

	minute='*/15' 				#(for every quarter) or minute='1,13,30-45,50-59/2'.
	
	hour='*/3' 					#(for every three hours) or hour='0,8-17/2' (at midnight, and every two hours during office hours).
	
	day_of_week='mon-fri' 		#(for weekdays only). (Beware that day_of_week='*/2' does not literally mean ‘every two days’, but ‘every day that is divisible by two’!)
	
	day_of_month='2-30/3' 		#(for every even numbered day) or day_of_month='1-7,15-21' (for the first and third weeks of the month).
	
	such as month_of_year='*/3' #(for the first month of every quarter) or month_of_year='2-12/2' (for every even numbered month).
	
	
# step4 启动worker
celery -A django_commitity beat -l info  # 多了beat


# 配置定时任务的另一种方法： 使用admin管理定时任务或者周期任务

	-- pip install django-celery-beat
	
	-- 添加'django_celery_beat' 到install_apps
	
	-- python manage.py migrate
	
	-- celery -A django_commitity beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
	
	
	# 登录admin页面，有4张表：crontabs, intervals, periodic tasks, solar events
	
	-- 点击periodic tasks 新建
	