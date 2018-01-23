# 选择序列化model的字段

"""
http://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields
"""

# step1 自定义一个序列化类DynamicFieldsModelSerializer
	class DynamicFieldsModelSerializer(serializers.ModelSerializer):
		"""
		A ModelSerializer that takes an additional `fields` argument that
		controls which fields should be displayed.
		"""

		def __init__(self, *args, **kwargs):
			# Don't pass the 'fields' arg up to the superclass
			fields = kwargs.pop('fields', None)

			# Instantiate the superclass normally
			super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

			if fields is not None:
				# Drop any fields that are not specified in the `fields` argument.
				allowed = set(fields)
				existing = set(self.fields.keys())
				for field_name in existing - allowed:
					self.fields.pop(field_name)
				
				
# step2 对model进行序列化

	class UserSerializer(DynamicFieldsModelSerializer):
		class Meta:
		model = User
		fields = ('id', 'username', 'email')

# step3 使用
	print UserSerializer(user)
	{'id': 2, 'username': 'jonwatts', 'email': 'jon@example.com'}

	print UserSerializer(user, fields=('id', 'email'))
	{'id': 2, 'email': 'jon@example.com'}