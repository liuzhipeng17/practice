# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


# User = get_user_model()


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"昵称")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号码")


class Teacher(models.Model):
    student = models.OneToOneField(UserProfile, null=True, blank=True, verbose_name=u"学生")


@receiver(post_save, sender=UserProfile, dispatch_uid="user_profile_post_save")
def create_teacher(sender, instance, created, **kwargs):
    if created:
        try:
            Teacher.objects.get(student_id=instance.id)
        except ObjectDoesNotExist as e:
            teacher = Teacher()
            teacher.student = instance
            teacher.save()




