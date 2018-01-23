
class Article(models.Model):
    STATUS_CHOICES = (
        (0, '发布'),
        (1, '删除'),
        (2, '下架')
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    abstract = models.CharField(max_length=255, blank=True)
    time_created = models.DateTimeField(default=timezone.now)
    author_id = models.PositiveIntegerField()
    author_name = models.CharField(max_length=30, blank=True)
    ad_id = models.PositiveIntegerField(null=True)
    image_id = models.PositiveIntegerField(null=True)
    source = models.CharField(max_length=30, blank=True)
    front_image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-time_created']



class ArticleSerializer(DynamicFieldsModelSerializer):
    """
    required=False表示反序列化的时候，不需要改字段。
    allow_blank=True,用户提交该字段的值为空，也是合法的
    allow_null是指在序列化的时候，可以为空的;即query_set里面的author_id可以为空，return Response不会报错
    required=False，在反序列化的时候，不用提供title。都可以不用提交该字段
    read_only=True, 表示用户更新或创建的时候，不用该字段；但是序列化的时候，会有该字段。
    """
    source = serializers.CharField(allow_blank=True, required=False)    # 可以不填的，但填了也是有好处的
    title = serializers.CharField()# 必填
    body = serializers.CharField() # 必填。在不是详情的情况下，这个字段不能序列化，否则会增加数据的困难
    abstract = serializers.CharField(allow_blank=True)# 你不用填，但是需要反序列化
    author_id = serializers.IntegerField(required=False)# 不要用户填
    author_name = serializers.CharField(required=False)# 不要用户填
    status = serializers.ChoiceField(choices=((1, u'上线'), (2, '下架'), (3, u'删除')), default=1)

    # method, read_only默认是True, 即不用提交这个字段，会将其序列化
    front_image = serializers.SerializerMethodField()
    comment_num = serializers.SerializerMethodField()
    read_num = serializers.SerializerMethodField()
    favor_num = serializers.SerializerMethodField()
    can_favor = serializers.SerializerMethodField()
    time_created = serializers.DateTimeField(allow_blank=True, required=False)

    def get_front_image(self, obj):
        if isinstance(obj, Article):
            return obj.front_image.url if obj.front_image else ''

    def get_comment_num(self, obj):
        if isinstance(obj, Article):
            return len(Comment.objects.filter(article_id=obj.id))

    def get_read_num(self, obj):
        if isinstance(obj, Article):
            return len(ArticleRead.objects.filter(article_id=obj.id))

    def get_favor_num(self, obj):
        if isinstance(obj, Article):
            return len(ArticleFavor.objects.filter(article_id=obj.id))

    def get_can_favor(self, obj):# 限制一个ip只能点赞一次
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

    def validate_abstract(self, value):
        if value is not None:
            return value
        else:
            body = self.initial_data.get('body')
            if len(body) > 20:
                return body[0:20]
            else:
                return body

    class Meta:
        model = Article
        fields = ('source', 'title', 'body', 'abstract', 'author_id','author_name','status','front_image',
                  'comment_num','read_num','favor_num','can_favor', 'time_created')
        read_only_fields = ('author_id', 'author_name',)