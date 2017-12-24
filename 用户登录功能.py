# django 加载静态页面的view

	from django.views.generic import TemplateView
	
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
