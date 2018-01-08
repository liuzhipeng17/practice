使用django来获取用户访问的IP地址，如果用户是正常情况下

通过request.META['REMOTE_ADDR']  可以获得用户的IP地址。

但是有些网站服务器会使用ngix等代理http，或者是该网站做了负载均衡，导致使用remote_addr抓取到的是1270.0.1，
这时使用HTTP_X_FORWARDED_FOR才获得是用户的真实IP。


推荐使用以下代码:

	if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
		ip =  request.META['HTTP_X_FORWARDED_FOR']  
	else:  
		ip = request.META['REMOTE_ADDR']  