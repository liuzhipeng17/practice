class PostSerializer(serializers.ModelSerializer):
    fav = serializers.SerializerMethodField('likedByUser')

    def likedByUser(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            try:
                liked=Favorite.objects.filter(user=request.user, post=obj.id).count()
                return liked == 1
            except Favorite.DoesNotExist:
                return False
        return "error"

    class Meta:
        model = Post


class PostView(APIVIEW):
     def get(self,request):
         serializers = PostSerializer(PostObjects,context={'request':request})
		 
		 
		 
# 记住一定是在get的里面的serializer传递参数context={'request': request}, 不是在post里面