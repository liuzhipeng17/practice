# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.core.cache import cache


class ConfirmPasswordValidator(object):
    # 通过传递用户第一次提交的password名字（记住是名字不是password的值）来进行实例化
    def __init__(self, password_field):
        self.password = password_field

    def set_context(self, serializer_field):
        self.serializer_field = serializer_field

    def __call__(self, value):
        password_confirm = value
        # 获取serializer,然后才能获取到用户提交的password
        serializer = self.serializer_field.parent
        raw_password = serializer.initial_data.get(self.password)
        try:
            # 这里是先对用户提交的password进行验证，验证的规则是password的validation
            password = serializer.fields.get(self.password).run_validation(raw_password)
        except serializers.ValidationError:
            return # 终止

        if password_confirm and raw_password and password_confirm !=raw_password:
            raise serializers.ValidationError('The two passwords you typed do not match ')


class SmsCodeValidator(object):
    def __init__(self, mobile_field):
        self.mobile = mobile_field

    def set_context(self, serializer_field):
        self.serializer_field = serializer_field

    def __call__(self, value):
        sms_code = value
        serializer = self.serializer_field.parent
        raw_mobile = serializer.initial_data.get(self.mobile)

        try:
            serializer.fields.get(self.mobile).run_validation(raw_mobile)
        except serializers.ValidationError:
            return

        cache_sms_code = cache.get(raw_mobile)
        if not cache_sms_code:
            raise serializers.ValidationError('Verification code is expired, please get again')

        if cache_sms_code and sms_code and cache_sms_code.lower() != sms_code.lower():
            raise serializers.ValidationError('Verification code is incorrect, please try again')
			
			
# 然后使用
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from django.core.cache import cache

from .validators import SmsCodeValidator, ConfirmPasswordValidator

user_model = get_user_model()


class RegisterVerifyCodeSerializer(serializers.Serializer):
    """
    获取验证码：只需要一个手机号(邮箱)，如果采用model（比如verifyCode表来存数据，但是基本上我们设置code
    字段为必填项。 那么注册的时候，就会要求填写那个注册验证码过来。（多余而且不知道验证是否成功）
    所以采用serializers.Serializers，而不用serializers.ModelSerializer
    对手机号验证：
        1 唯一性 UniqueValidator
        2 合法性1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        3 频率(5分钟内不允许重复获取）--设置cache的存活时间为5*60
    """
    mobile = serializers.CharField(max_length=11, min_length=11,
                                   validators=[RegexValidator(
                                       regex="^1[358]\d{9}$|^147\d{8}$|^176\d{8}$",
                                       message="invalid mobile number, please try again"),
                                   UniqueValidator(queryset=user_model.objects.all(),
                                                   message="This mobile already has been registered, please try again")])


class RegisterSerializer(RegisterVerifyCodeSerializer):
    """
    注册的时候，需要注册用户手机号，填写验证码，填写密码，二次密码
    """
    # mobile = RegisterVerifyCodeSerializer()
    password = serializers.CharField(write_only=True, required=True, max_length=16, min_length=6)
    password_confirm = serializers.CharField(write_only=True, required=True,
                                             validators=[ConfirmPasswordValidator('password')])
    sms_code = serializers.CharField(required=True, validators=[SmsCodeValidator('mobile')])
	
	
