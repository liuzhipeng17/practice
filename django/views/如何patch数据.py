	"""
	https://stackoverflow.com/questions/21148039/how-to-make-a-patch-request-using-django-rest-framework
	"""
# step1 确保你的APIView可以patch方法
	#Make sure that you have "PATCH" in http_method_names. Alternatively you can write it like this:

    @property
    def allowed_methods(self):
        """
        Return the list of allowed HTTP methods, uppercased.
        """
        if "patch" in self.http_method_names:
            pass
        else:
            self.http_method_names.append("patch")
        return [method.upper() for method in self.http_method_names
                if hasattr(self, method)]

				
# step2 为了允许update partial fields , 使用partial参数; 在你的APIView添加以下函数
	"""
		As stated in documentation:

		By default, serializers must be passed values for all required fields or they will raise validation errors. You can use the partial argument in order to allow partial updates.
		Override update method in your view:
	"""
	def patch(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = TimeSerializer(instance, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(customer_id=customer, **serializer.validated_data)
		return Response(serializer.validated_data)


# step3 在serializer需要overwrite update函数
	"""
	Serializer calls update method of ModelSerializer(see sources):
	"""
	def update(self, instance, validated_data):
		#raise_errors_on_nested_writes('update', self, validated_data)

		# Simply set each attribute on the instance, and then save it.
		# Note that unlike `.create()` we don't need to treat many-to-many
		# relationships as being a special case. During updates we already
		# have an instance pk for the relationships to be associated with.
		for attr, value in validated_data.items():
			setattr(instance, attr, value)
		instance.save()

		return instance
		
