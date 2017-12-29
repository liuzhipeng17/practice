# 自定义用户


# step1 member/models.py 自定义manager, user

	# 先说官网的自定义
	# https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#custom-users-and-proxy-models

			
	# 接下来说说别人的自定义
	# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html


# 接下来是大招：制作自己的自定义模板(设计原则：尽量减少存储。如果一些属性不是必要做展示，但是也是需要知道的，可以通过属性来做；）
"""
需要注意的是，自定义User，继承AbstractBaseUser， django的验证机制就不适合user,你需要其他认证机制。 我这里选择的第三方包: djangorestframwork-jwt。
是一种基于token的验证机制。和drf内置的token有很多不同。不需要将token存储在数据库里。


"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=255)# 用email来注册，email不能为空
    mobile = models.CharField(_('mobile_number'), blank=True, max_length=11)
    fullname = models.CharField(_('full name'), blank=True, max_length=127)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
	is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	
    objects = UserManager()

    USERNAME_FIELD = 'email'  # 注意这个属性：USERNAME_FIELD, email必须是唯一的字段，
    REQUIRED_FIELDS = []
    # 通过命令createsuperuser 或者createuser 创建用户的时候，必填的选项； 这和上面表字段设计有关系，
    # 如果没有默认值的， 都要加到这里

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

	def __str__(self):
		return self.email
	
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
		

# 还需要自定义一个UserManger
# member/managers.py
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, **extra_fields):
        """
        Creates and saves a User with the given email and password.
		staff就是superuser(admin)，能登录后台管理页面的用户
        """
        if not email:
            raise ValueError('The given email must be set')
		
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, False, **extra_fields)
	
		
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, True, **extra_fields)
		

# 接着 需要配置settings.py

AUTH_USER_MODEL = 'member.User'


# 如何引用我们的User呢？
	不推荐： from member.models import User
	推荐使用这种：
	from django.db import models
	from django.conf import settings

	class Course(models.Model):
		slug = models.SlugField(max_length=100)
		name = models.CharField(max_length=100)
		tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
		# 通过settings.AUTH_USER_MODEL来引用

# 这种自定义是需要自己定义用户验证的，不能用django的用户验证。-- 但是我们可以自定义用户的字段，不必想django那么多的字段（浪费空间）
# 后面再总结