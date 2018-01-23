    def put(self, request, uid, article_id, format=None):
        self.get_user_object(uid)
        article = self.get_object(article_id)
        serializer = self.serializer_class(article, data=request.data) # 注意这里
        if serializer.is_valid():
            serializer.save()
            # 并没有执行update函数, 而是执行了create函数，这是为啥
            # 这是因为self.serializer_class的参数和update的参数不匹配
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
		
		
# 
"""
	serializer = self.serializer_class(article, data=request.data) # 注意这里

	和serializer的update()参数匹配def update(self, instance, validated_data):
"""