
""" 
	在web开发中, 你可能会遇到下面这种场景:
	在用户完成某个操作后, 自动去执行一些后续的操作. 譬如用户完成修改密码后,你要发送一份确认邮件

	观察者模式：观察者模式(Observer)完美的将观察者和被观察的对象分离开。
		举个例子，用户界面可以作为一个观察者，业务数据是被观察者，
		用户界面观察业务数据的变化，发现数据变化后，就显示在界面上
"""

"""学习网站https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html"""

"""两个重要的对象：Sender receiver 
		 sender dispatch a signal, receiver receive signal and do something
		 sender 是一个object, receiver是一个方法，或者对象的方法
		 将sender和receiver关联起来是通过signal dispatchers, 即Signal.connect()方法来关联sender,receiver
"""

# 方式1粗劣使用(下面有这种方式的改进）

		# post_save信号
		""" 在mode对象执行save函数时，就会触发该信号"""

		from django.contrib.auth.models import User
		from django.db.models.signals import post_save

		def save_profile(sender, instance, **kwargs):
			instance.profile.save()

		post_save.connect(save_profile, sender=User)


		# save_profile是receiver，User是sender, post_save是signal, 上面代码可以理解成：当User对象执行save函数后，就会执行save_profile函数

		# 如果去掉post_save.connect的sender参数，如： post_save.connect(save_profile)， 则就是任意一个model执行了save函数，都会调用save_profile函数



# 方式2 使用（推荐）

	# 注册信号不应该在app的models或者根目录，django建议我们将signals放到config里面，以下面为了，profile为一个app；cmdbox是project

	# step1 
		# profile/signals.py
		from django.contrib.auth.models import User
		from django.db.models.signals import post_save
		from django.dispatch import receiver

		from cmdbox.profiles.models import Profile

		@receiver(post_save, sender=User)
		def create_user_profile(sender, instance, created, **kwargs):
			if created:
				Profile.objects.create(user=instance)

		@receiver(post_save, sender=User)
		def save_user_profile(sender, instance, **kwargs):
			instance.profile.save()

		""" instance参数就是sender的实例化对象"""
	
	# step2 
		#profiles/app.py:
		from django.apps import AppConfig
		from django.utils.translation import ugettext_lazy as _

		class ProfilesConfig(AppConfig):
			name = 'cmdbox.profiles'
			verbose_name = _('profiles')

			def ready(self):
				import cmdbox.profiles.signals  # noqa
	
	# step3
			
		# profiles/__init__.py: 如果已经在工程里面注册了app,这里是不需要的
		default_app_config = 'cmdbox.profiles.apps.ProfilesConfig'





# 方式3（方式1的改进）

	# 通过connect关联sender和receiver,参考下面代码

	# step1 
		# profile/signals.py
		from cmdbox.profiles.models import Profile

		def create_user_profile(sender, instance, created, **kwargs):
			if created:
				Profile.objects.create(user=instance)

		def save_user_profile(sender, instance, **kwargs):
			instance.profile.save()

	# step2
		# profile/app.py
		from django.apps import AppConfig
		from django.contrib.auth.models import User
		from django.db.models.signals import post_save
		from django.utils.translation import ugettext_lazy as _

		from cmdbox.profiles.signals import create_user_profile, save_user_profile

		class ProfilesConfig(AppConfig):
			name = 'cmdbox.profiles'
			verbose_name = _('profiles')

			def ready(self):
				post_save.connect(create_user_profile, sender=User)
				post_save.connect(save_user_profile, sender=User)
	
	# step3 
		# profiles/__init__.py:
		default_app_config = 'cmdbox.profiles.apps.ProfilesConfig'
