# https://www.v2ex.com/t/343618

# https://segmentfault.com/a/1190000010080849?utm_source=itdadao&utm_medium=referral

# Dynamically modifying fields 动态修改字段

"""
有这种场景，比如查看用户的信息，对于好友，本人，以及游客看到的信息是不一样的，比如Password肯定是只能本人可以看到的
但是都是同样使用UserSerializer，
那么如何对这些fields做一些限制呢？从而只需要序列化一个UerSerializer类，然后根据传递参数得到多个serializer 对象

动态序列化字段

"""
"""
一旦序列化程序初始化完毕，就可以使用.fields属性访问在序列化程序中设置的字段字典。 
访问和修改这个属性允许你动态地修改序列化。

直接修改fields参数允许你做一些你感兴趣的事情，比如在运行时，改变序列化哪些字段，而不是在声明序列化的时候。

"""

# step1 声明一个serializer基础类，可以动态序列化fields

	class DynamicFieldsModelSerializer(serializers.ModelSerializer):
		"""
		A ModelSerializer that takes an additional `fields` argument that
		controls which fields should be displayed.
		"""

		def __init__(self, *args, **kwargs):		# 很明显通过**kwargs传递fields参数， fields=[], 这样就会只序列化fields里面的字段
			# Don't pass the 'fields' arg up to the superclass
			fields = kwargs.pop('fields', None)

			# Instantiate the superclass normally
			super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

			if fields is not None:
				# Drop any fields that are not specified in the `fields` argument.
				allowed = set(fields)
				existing = set(self.fields.keys())	# existing是class Meta里定义的fields
				for field_name in existing - allowed:
					self.fields.pop(field_name)
				
# step2 声明序列化（这个时候是最好把所有字段都列出，在运行的时候在通过fields参数，来绝对序列化哪些字段）

	class UserSerializer(DynamicFieldsModelSerializer):
		class Meta:
			model = User
			fields = ('id', 'username', 'email')
			
# step3 使用

	print UserSerializer(user)
	#{'id': 2, 'username': 'jonwatts', 'email': 'jon@example.com'}

	print UserSerializer(user, fields=('id', 'email'))	# 通过传递fiels，来只序列化id和email字段
	#{'id': 2, 'email': 'jon@example.com'}