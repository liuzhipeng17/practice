# django执行定时任务


"""
# 1安装第三方包django-crontab
	pip install django-crontab
	
# 2将"django-crontab" 添加到install-apps

# 3自定义django-admin命令 test_cm


# 4 添加任务到计划表 settings.py
	CRONJOBS = [
    ('*/5 * * * *', 'django.core.management.call_command', ['test_cm']),
	]

$5 加载任务
	python manage.py crontab add
"""


# 备注：
"""

# 将定时任务的结果存放到文件
CRONJOBS = [
    ('47 11 * * *', 'django.core.management.call_command', ['test_cm']，{},'>> /var/run.log'),
]


# 
django-crontab任务加载比较简单，只需要运行 python manage.py crontab add 即可
查看已经激活的任务使用 python manage.py crontab show
删除已经有的任务使用 python manage.py crontab remove
如果你修改了任务记得一定要使用 python manage.py crontab add 这个会更新定时任务

"""

