# custom serializer field validator and custom serialzer validation(Field_level, Object_level)
	
"""
这里主要介绍：custom field valiation, custom validator, custom valiationerror message

"""

# step1 validate_field   
	
		# 要求field必须serializer的字段

		# 下面是一个验证mobile的（但是你会发现，我们还需要验证的正则表达式； 由于不是继承ModelSerializer所以加上唯一性的验证）

		class RegisterVerifyCodeSerialzer(serializers.Serializer):
			mobile = serializers.CharField(max_length=11, min_length=11)
			def validate_mobile(self, mobile):
				try:
					user_model.objects.get(mobile=mobile)
					raise serializers.ValidationError("mobile has been registed")
				except user_model.DoesNotExist:
					return mobile  # 这个值必须返回
					
		
		# 其实这个唯一性：可以直接继承from rest_framework.validators import UniqueValidator
		
		
			# -*- coding: utf-8 -*-

			from django.contrib.auth import get_user_model # If used custom user model
			from rest_framework import serializers
			from rest_framework.validators import UniqueValidator
			from django.core.validators import RegexValidator

			user_model = get_user_model()


			class RegisterVerifyCodeSerialzer(serializers.Serializer):
				"""
				"""
				mobile = serializers.CharField(max_length=11,
												min_length=11,
											    validators=[RegexValidator(
																		regex="^0?(13[0-9]|14[56789]|15[012356789]|166|17[012345678]|18[0-9]|19[89])[0-9]{8}$",
																		message=u"invalid mobile number"),
															UniqueValidator(queryset=user_model.objects.all(),
																		message="This mobile already has been registered")
																		]
																		)

					
# step2 validate
	from rest_framework import serializers

	class EventSerializer(serializers.Serializer):
		description = serializers.CharField(max_length=100)
		start = serializers.DateTimeField()
		finish = serializers.DateTimeField()

		def validate(self, data):
			"""
			Check that the start is before the stop.
			"""
			if data['start'] > data['finish']:
				raise serializers.ValidationError("finish must occur after start")
			return data
			
# step3 自定义validator, 不是validation


	# function based validator
	def validate_20mb_size(value):
		max_size = 1024 * 1024 * 20
		if value.size > max_size:
			raise serializers.ValidationError('profile Image is too large')
		
	# then we use like this
	profile_dict = serializers.ImageField(validators=[validate_20mb_size])

	# Class based validtor
	class ImageSizeValidtor(object):
		def __init__(self, max_size):
			self.max_size = 1024 * 1024 * max_size
			
		def __call__(self, value):
			if value.size > self.max_size:
				raise  serializers.ValidationError('profile Image is too large')

	# then we user like this
	profile_dict_c = serializers.ImageField(validators=[ImageSizeValidtor(max_size=20)])
		
		
	# 补充
	 # 自定义validator， 可以定义一些公用field都用到的validator,也可定义某个field用到的validator


	# my_app/validators.py
	def validate_required(value):
		# whatever validation logic you need
		if value == '' or value is None:
			raise serializers.ValidationError('This field is required.')

	# my_app/serializers.py
	class MyModelSerializer(serializers.ModelSerializer):

		class Meta:
			model = MyModel
			extra_kwargs = {"field1": {"validators": [validators.validate_required,]}}
			
		
		
# step4 自定义error_message（有时候想重写model的唯一验证UniqueValidator的错误信息)
  用户注册的时候， usrname当遇到unqiueValidator验证异常的时候，错误信息为：{'username': [u'This field must be unique.']}
  向将错误信息改成：This username is already taken. Please try again
  
  我们可以通过extra_kwargs来定义unique的错误信息
  
  class Meta:
    extra_kwargs = {"username": {"validators": [validators.UniqueValidator(message="This username is already taken. Please try again")]}
	
  # 或者
	mobile = serializers.CharField(validators=[UniqueValidator(queryset=user_model.objects.all(),message="This mobile already has been registered")])

	
  # 如果还想增加一个regrex的验证: 查看step3的做法
  from django.core.validators import RegexValidator
	
  	class GameRecord(serializers.Serializer):
		mobile = serializers.CharField(validators=[RegexValidator(regex="^139[0-9]{8}", message="", code="c1")])
  
  
  

			
# step5 向用户注册的序列化（最好不要继承ModelSerialzier)
"""
因为注册的时候，需要填写： 用户名，密码，验证码，二次密码确认，最好继承Serializr.serializer
"""
  