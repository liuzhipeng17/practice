# django执行定时任务


"""
# 1安装第三方包django-crontab
	pip install django-crontab
	
# 2将"django-crontab" 添加到install-apps

# 3自定义django-admin命令


# 4 添加任务到计划表 settings.py
	CRONJOBS = [
    ('*/5 * * * *', 'django.core.management.call_command', ['xxxx']),
	]

$5 执行任务
	python manage.py crontab add
"""


