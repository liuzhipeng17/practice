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
                                                   message="This mobile already has been registered, please try again")])

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
	#project.url
	urlpatterns = [
		url(r'^admin/', admin.site.urls),
		url(r'^api-auth/', obtain_jwt_token, name='obtain_jwt_token'),  # POST email=email&password=password
		url(r'^v1/member/', include('member.urls', namespace="member")),
	]
	#app.url
	urlpatterns = [
		url(r'^registersmscode/$', RegisterSmsCodeAPIView.as_view(), name='obtain_jwt_token'),  # POST email=email&password=password

	]

	
# step3 定义view

	# -*- coding: utf-8 -*-
	from rest_framework.views import APIView
	from django.core.cache import cache
	from rest_framework.response import Response
	from rest_framework import status

	from member.serializers import RegisterVerifyCodeSerialzer
	from utils.yunpian import generate_code,generate_random_code


	class RegisterSmsCodeAPIView(APIView):
		serializer_class = RegisterVerifyCodeSerialzer

		def post(self, request, format=None):
			serializer = self.serializer_class(data=request.data)
			if serializer.is_valid():
				# 生成随机验证码，并存储到cache,并发送验证码到邮箱上（还没开通云片网）
				email_code = generate_random_code(email='229318714@qq.com', random_length=5)
				data = {'message': 'success', 'email_code': email_code, 'code': 2000}
				return Response(data=data, status=status.HTTP_201_CREATED)
			else:
				data = {'message': serializer.errors, 'code': 2001}
				return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



# step4 产生随机验证码
	# -*- coding: utf-8 -*-
	import random
	from django.core.cache import cache
	from django.core.mail import EmailMessage


	#生成验证码
	def generate_code(num, mobile):
			veri_code = ''.join([ str(random.choice(range(0,10))) for i in range(num) ])
			cache.set(mobile,veri_code,timeout=3600)
			return veri_code


	def generate_random_code(email=None, random_length=8):
		"""
		生成8位随机字母或数字
		"""
		temp_char = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqXxYyZz0123456789"
		length = len(temp_char)
		str = ""
		for i in range(0, random_length):
			str += temp_char[random.randint(0, length - 1)]

		if email:
			# 发送数据给邮箱
			print "hello"
			email_message = EmailMessage(u'刘志鹏网站注册验证码', u'您的验证码为{0}'.format(str), from_email='liucpliu@sina.cn', to=[email])
			email_message.send()
			cache.set(email, str, timeout=3600)
			# 将数据保存在cache里一个小时

		return str

	if __name__ == "__main__":
		print generate_random_code()

