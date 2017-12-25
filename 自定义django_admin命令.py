"""
自定义django-admin命令test_cm, 使得其在终端按以下格式执行 python manage.py test_cm


首先在你的app目录下新建 python package: mamagement
然后在你的management目录新建python package: commands
  
接着在commands目录新建python文件test_cm.py
  
"""
  
# 编写test_cm.

# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from crontab.models import UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_list = UserProfile.objects.all()
        count = len(user_list)
        print count

		
# 在cmd终端运行：python manage.py test_cm 测试命令是否正常