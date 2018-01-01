# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model # If used custom user model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

user_model = get_user_model()


class RegisterVerifyCodeSerialzer(serializers.Serializer):
    """
    获取验证码：只需要一个手机号(邮箱)，如果采用model（比如verifyCode表来存数据，但是基本上我们设置code
    字段为必填项。 那么注册的时候，就会要求填写那个注册验证码过来。（多余而且不知道验证是否成功）
    所以采用serializers.Serializers，而不用serializers.ModelSerializer
    由于没有采用ModelSerializer， 所以一定要验证mobile的唯一性。
    如果是继承ModelSerializer<, 他会自带的Unique， 可以repr(类对象）来验证
    """
    mobile = serializers.CharField(max_length=11, min_length=11,
                                   validators=[RegexValidator(
                                       regex="^0?(13[0-9]|14[56789]|15[012356789]|166|17[012345678]|18[0-9]|19[89])[0-9]{8}$",
                                       message=u"invalid mobile number"),
                                   UniqueValidator(queryset=user_model.objects.all(),
                                                   message="This mobile already has been registered")])

    # def validate_mobile(self, mobile):
    #     # 对mobile进行验证
    #     # 1 验证是否注册，（如果是继承了ModelSerializer，它会自验证它的validator: unique）
    #             # 因为mobile是user里面设置unique；但是这里不是用ModelSerializer所以必须要进行压着
    #
    #     # 2 验证手机号码是否合法（正则表达式， 在这里搞）
    #     try:
    #         user_model.objects.get(mobile=mobile)
    #         raise serializers.ValidationError("This mobile already has been registed")
    #     except user_model.DoesNotExist:
    #         return mobile  # 这个值必须返回




# step2 定义url


# step3 定义view







