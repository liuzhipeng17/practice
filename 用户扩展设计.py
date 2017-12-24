# -*- encoding: utf-8 -*-
"""
扩展django自带的user, auth.user表
id， password, last_login, is_superuser, username,
first_name, last_name, email, is_staff, is_active,
date_joined

这些无法满足我们用户的需要： 
nickname, birthday, gender, address, mobile, avatar
需要自定义user, 继承原有的user下扩展
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    """用户信息
    """
    nickname = models.CharField(max_length=32, verbose_name=u"昵称", default=u"")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name=u"性别", default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(upload_to="images/%Y/%m", default="images/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
        # username已经是UserProfile的字段


# 还需要一个邮箱验证码（注册和找回密码都需要用到）， 建立一个model

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name = u"邮箱")
    type = models.CharField(max_length=10, choices=(("register", u"注册"), ("forget", u"找回密码")), verbose_name=u"类型")
    time_sended = models.DateTimeField(default=datetime.datetime.now)
    # now后面不要加(), 区别就是加()，在编译EmaliVerifyRecord就会加进去， 而不是实例化对象的时候加入

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}--{1}'.format(self.code, self.email)


# 轮播图banner

class IndexBanner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"轮播顺序")
    time_add = models.DateTimeField(auto_now=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"首页轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
