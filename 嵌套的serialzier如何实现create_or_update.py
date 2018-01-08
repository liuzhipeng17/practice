# create or update in nested serializer（stackflow的例子）

	# step1 model的设计（采用外键）
		class Book(models.Model):
			title = models.CharField(max_length=50)


		class Page(models.Model):
			book = models.ForeignKey(Books, related_name='related_book')
			text = models.CharField(max_length=500)
			
	# step2 序列化
		class PageSerializer(serializers.Serializer):
			text = serializers.CharField(max_length=500)

		class BookSerializer(serializers.Serializer):
			page = PageSerializer(many=True)
			title = serializers.CharField(max_length=50)

			def create(self, validated_data):
				# Create the book instance
				book = Book.objects.create(title=validated_data['title'])

				# Create or update each page instance
				for item in validated_data['pages']:
					page = Page(id=item['page_id'], text=item['text'], book=book)
					page.save()

				return book
				
	# step3 更新update函数

	"""
	可以看到仅仅通过book的post上page的数据，从而创建page和book, 但是并不支持update page数据
	"""

		def update(self, instance, validated_data):
			# Update the book instance
			instance.title = validated_data['title']
			instance.save()

			# Delete any pages not included in the request
			page_ids = [item['page_id'] for item in validated_data['pages']]
			for page in instance.books:
				if page.id not in page_ids:
					page.delete()

			# Create or update page instances that are in the request
			for item in validated_data['pages']:
				page = Page(id=item['page_id'], text=item['text'], book=instance)
				page.save()

			return instance
			
			
# 我自己的例子
	class ArticleImageSerializer(serializers.ModelSerializer):
		image = Base64ImageField(use_url=True, allow_empty_file=True)
		id = serializers.IntegerField(default=0)  # because the id is must required when update image

		class Meta:
			model = ArticleImage
			fields = ('image', 'id')


	class ArticleSerializer(DynamicFieldsModelSerializer):
		# author_id = serializers.IntegerField()
		source = serializers.CharField(allow_blank=True)
		title = serializers.CharField()
		body = serializers.CharField()
		abstract = serializers.CharField(allow_blank=True)
		status = serializers.ChoiceField(choices=((0, u'上线'), (1, '下架'), (2, u'删除')), default=1)
		article_images = ArticleImageSerializer(many=True)
		front_image = Base64ImageField(use_url=True, allow_empty_file=True)
		# front_image = serializers.SerializerMethodField()
		comment_num = serializers.SerializerMethodField()
		read_num = serializers.SerializerMethodField()
		favor_num = serializers.SerializerMethodField()
		can_favor = serializers.SerializerMethodField()
		author = serializers.SerializerMethodField()

		def get_author(self, obj):
			if isinstance(obj, Article):
				author = User.objects.get(id=obj.author_id)
				return UserInfoSerializer(author).data

		# def get_front_image(self, obj):
		#     if isinstance(obj, Article):
		#         return obj.front_image.url if obj.front_image else ''

		def get_comment_num(self, obj):
			if isinstance(obj, Article):
				return len(Comment.objects.filter(article_id=obj.id))

		def get_read_num(self, obj):
			if isinstance(obj, Article):
				return len(ArticleRead.objects.filter(article_id=obj.id))

		def get_favor_num(self, obj):
			if isinstance(obj, Article):
				return len(ArticleFavor.objects.filter(article_id=obj.id))

		def get_can_favor(self, obj):  # 限制一个ip只能点赞一次
			if isinstance(obj, Article):
				# 获取远程请求的ip地址(根据远程request）
				request = self.context.get("request")
				# 这里在serializer = AccountSerializer(account, context={'request': request})
				if request:
					if request.META.has_key('HTTP_X_FORWARDED_FOR'):
						ip = request.META['HTTP_X_FORWARDED_FOR']
					else:
						ip = request.META['REMOTE_ADDR']

					return not ArticleFavor.objects.filter(article_id=obj.id, ip=ip).exists()

		def create(self, validated_data):
			article_images_data = validated_data.pop('article_images')
			front_image = validated_data.pop('front_image')
			author_id = self.context.get('request').user.id
			validated_data.update({'author_id': author_id})
			# create article instance
			article = Article.objects.create(**validated_data)
			article.front_image = front_image
			article.save()
			# create article_image instance
			for article_image in article_images_data:
				image = article_image.pop('image')
				article_image.pop('id')
				temp = ArticleImage.objects.create(article_id=article.id, **article_image)
				temp.image = image
				temp.save()
			return article

		def update(self, instance, validated_data):
			article_images_data = None
			if validated_data.has_key('article_images'):
				article_images_data = validated_data.pop('article_images')
			for attr, value in validated_data.items():
				setattr(instance, attr, value)
			instance.save()
			# if article_images id is 0, it is mean to add image or will be update image
			if article_images_data is not None:
				image_ids = [item['id'] for item in article_images_data]
				images = ArticleImage.objects.filter(article_id=instance.id)
				if images.exists():
					for image in images:
						if image.id not in image_ids:
							image.delete()
				# create or update image instances that are in the request
				for item in article_images_data:
					if item['id']==0:
						# article_image = ArticleImage.objects.create(article_id=instance.id, image=item['image'])
						article_image = ArticleImage.objects.create(article_id=instance.id)
						article_image.image = item['image']
					else:
						# article_image = ArticleImage(id=item['id'], article_id=instance.id, image=item['image'])
						article_image = ArticleImage(id=item['id'], article_id=instance.id)
						article_image.image = item['image']
					article_image.save()
			return instance

		class Meta:
			model = Article
			fields = ('source', 'title', 'body', 'abstract', 'author', 'status', 'front_image',
					  'comment_num', 'read_num', 'favor_num', 'can_favor', 'time_created', 'article_images', 'id',
					  )
			read_only_fields = ('id', 'time_created')

		def validate_abstract(self, abstract):
			body = self.initial_data.get('body', '')
			if not abstract and body:
				abstract = body[0:127] if len(body) > 128 else body

			return abstract

