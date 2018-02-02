#The 'avatar' attribute has no file associated with it.

# 当出现上述问题时，大部分都是imageField的upload_to属性导致的问题

# 官网教程
https://docs.djangoproject.com/en/1.9/howto/static-files/#serving-files-uploaded-by-a-user-during-development

# 一篇好博客
http://blog.csdn.net/sherlockzoom/article/details/51910171

class BlogContent(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField()
	
	
Your image would be upload to media folder, so beter change path in model like images/, and they will be upload to media/images

# settings.py 添加

	MEDIA_URL = '/media/'
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# url.py添加

from django.conf.urls.static import static
from django.conf import settings

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# view
And then, if you want to display all this image, use something like this in view.py
	objects = BlogContent.objects.all()
	并将这个objects返回

# 在template这么渲染
And render it like this:

{% for img in objects %}
	<img src="{{ img.image.url }}" >
{% endfor %}