class Article(models.Model):
    STATUS_CHOICES = (
        (0,'unpublish'),
        (1,'published'),
        (2,'disable'),
    )
    ARTICLE_CHOICES = (
        (0,'news'),
        (1,'topic'),
    )
    title = models.CharField(max_length=200,db_index=True)
    body = models.TextField()
    image = models.ImageField(upload_to='article/%Y/%m/%d',null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,default=1)
    article_type = models.IntegerField(choices=ARTICLE_CHOICES)
    abstract = models.CharField(max_length=255,blank=True,null=True)
    source = models.CharField(max_length=54,blank=True)
    views = models.ManyToManyField(Views,related_name='article_views')
    author = models.ForeignKey(Profile,related_name='article_user',null=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,related_name='article_category',blank=True,null=True)
    tags = models.ManyToManyField(Tags,related_name='article_tags')


    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        super(self.__class__,self).save(*args,**kwargs)
        if len(self.tags.all()) == 1:
            try:
               es_data = {}
               id = self.id
               es_data['title'] = self.title  
               es_data['id'] = self.id 
               es_data['source_type'] = 1
               es_data['body'] = self.body
               es_data['status'] = self.status
               es_data['article_type'] = self.article_type
               es_data['article_views_count'] = len(self.views.all())
               es_data['created_at'] = self.created_at
               es_data['image_url'] = self.image.url if self.image  else  '' 
               try:
                  es_data['author']  = self.author.personal_info.name 
               except Exception as e:
                  print e
               try:
                  es_data['category'] = self.category.name
               except Exception as e:
                  es_data['category'] = None
           
               try:
                  es_data['tags'] = [  tag.name  for tag in self.tags.all() ]
               except Exception as e:
                  print e

               ES(mapping=articlemapping,index_name="post",doc_type="article").sync_es(es_data,id)
            except Exception as e:                print e
        
        elif len(self.tags.all()) >1:
              #pdb.set_trace()
              es.update(index="post",doc_type="article",id=self.id,body={'doc':{'tags':[  tag.name  for tag in self.tags.all() ]}})

    class Meta:
        ordering = ['-created_at']