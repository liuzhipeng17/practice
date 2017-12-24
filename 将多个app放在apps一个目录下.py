# -*- coding: utf-8 -*-
"""
	把多个app文件放在一个文件夹内，不然app过多，不好
	
"""

# step1  

"""
在工程的目录内，新建一个python package: apps
并将app 拷贝到apps内： 如果是通过Pycharm来做的话， 一定要去掉：search for references； 顺便去掉open moved fiels in editor（不打开移动文件）


# app内文件会报错：有些Import会红线； 会两步来解决
	1 apps右键mark source root; 原因是： 将apps作为资源，如果在root找不到，会到apps里面查找
	
	2 命令行运行python manage.py runserver 还是会报错（不是pycharm 的run)； 解决： 将apps 在settings.py里面设置可以在 python解析器搜索目录找到；
		
			import sys
			sys.path.insert(0, os.path.join(BASEDIR, 'apps'))
"""



# 备注
"""
当将所有app放在apps目录下后，如果修改model，然后执行python manage.py makemigrations ,python manage.py migrate 

此时会报错；主要原因是migrations下面， 有些参数多了apps, 将其参数中的apps.删除 

"""