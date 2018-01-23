# 如何将xadmin集成到project


# step1 github下载源码
	"""git clone https://github.com/sshwsfc/xadmin"""

# step2 根据requirements 下载依赖包
	"""
			django>=1.9.0  
			django-crispy-forms>=1.6.0
			django-import-export>=0.5.1
			django-reversion>=2.0.0
			django-formtools==1.0
			future==0.15.2
			httplib2==0.9.2
			six==1.10.0
			xlwt  --可选的，
			xlsxwriter --可选的
	"""
# step3 在你的工程新建python packages : extra_apps
	"""并右键 mark source root
	
	同时在settings.py里面将extra_apps目录添加到python的搜索目录内
	sys.path.insert(0, os.path.join(BASEDIR, "extra_apps"))
	"""

# step4 将xadmin应用添加到install_app里面
	"""
    'xadmin',
    'crispy_forms',
    'reversion',
	"""
# step5 设置xadmin后台的中文，和当地时区

LANGUAGE_CODE ="zh-hans"  # 1.8之后该
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = False  # 这个一定要改成False, 否则数据库的时间就是国际时间，UTC时间

# step6 迁移xadmin数据库

"""
python manage.py makemigrations
python manage.py migrate
"""
#可以看到多了四张表：xadmin-bookmark, xadmin-log, xadmin_usersettings, xadmin_userwidget


# step7 配置xadmin的url

import xadmin  

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]


# step8 
"""
	python manage.py createsuperuser 
	python manage.py runserver 127.0.0.1:9000
"""
# 浏览器网页127.0.0.1:9000/xadmin

# step9 注册models到xadmin
"""
在你的后台上，添加一个adminx.py文件

"""
# project/apps/users/adminx.py
# -*- coding: utf-8 -*-
import xadmin

from models import EmailVerifyRecord, UserProfile


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','type','time_sended']
    search_fields = ['code','email','type']
    filter_fields = ['code','email','type','time_sended']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

#step9 xadmin的全局配置
"""
	step: 主题配置
	

"""
from xadmin import views


class BaseSettingAdmin(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSettingAdmin)

# step10 设置网站名称和底部
class SiteSettingAdmin(object):
    site_title = u"深圳洪迈后台管理系统"
    site_footer = u"深圳洪迈有限公司"
	
xadmin.site.register(views.CommAdminView , SiteSettingAdmin)

# step11 将每个app下的model收缩
class SiteSettingAdmin(object):
    menu_style = "accordion"
	
# step12 设置app的中文名称， 以users app为例
	
"""
apps/users/apps.py 里面修改

"""
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name= u"用户管理"
	
# 同时还要在users下面的__init__.py添加以下内容“
default_app_config = "users.apps.UsersConfig"
