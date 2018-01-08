# 在django rest framework 这样说明
"""
Pagination is only performed automatically if you're using the generic views or viewsets. 
If you're using a regular APIView, you'll need to call into the pagination API yourself to ensure you return a paginated response.
 See the source code for the mixins.ListModelMixin and generics.GenericAPIView classes for an example.

"""

# 只有在viewsets或者generic views， 才会自动帮你实现分页（当然，前提是你做了配置）；常规的APIView,则需要自己去调用分页的API

# 采用django的分页，但是djangod的分页是没有上一页，下一页和当前页码的；而且是一次性返回所有数据（肯定不能这么干）

# https://stackoverflow.com/questions/29071312/pagination-in-django-rest-framework-using-api-view

# https://stackoverflow.com/questions/35525202/django-pagination-with-next-previous-count/35525458#35525458



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"contacts": contacts}
	
	
class ArticleAPIView(APIView):
	serializer_class = AritcleSerializer
	
	def get(self, request, format=None):
		page_size = self.query_params.get('page_size', 10)
		page = self.query_params.get('page', 1)
		
		article_list = Article.objects.filter(
