# 简单介绍下drf的认证机制
	# 不同于session的认证机制。 drf 的认证机制有四种：
		
		BasicAuthentication
		SessionAuthentication
		TokenAuthentication
		Custom authentication（自定义）
		
		
	# 一般将drf的认证机制存放在settings.py的一个列表'DEFAULT_AUTHENTICATION_CLASSES'里面。

	REST_FRAMEWORK = {
		'DEFAULT_AUTHENTICATION_CLASSES': (
			'rest_framework.authentication.BasicAuthentication',
			'rest_framework.authentication.SessionAuthentication',
		)
		# drf的其他设置
	}


	# 未认证可能的返回结果：
		HTTP 401 Unauthorized ： 401返回头字段里面有一个key:WWW-Authenticate , 
		
	# 禁止验证的返回结果
		HTTP 403 Permission Denied ： 403响应的头字段是没有WWW-Authenticate 的
		
		
	# BasicAuthentication： 对用户名和密码进行签名，大部分用于测试

# 如何使用drf TokenAuthentication

	-- step1 将TokenAuthentication 添加到settings.py的配置中
			REST_FRAMEWORK = {
				'DEFAULT_AUTHENTICATION_CLASSES': (
					'rest_framework.authentication.BasicAuthentication',
					'rest_framework.authentication.SessionAuthentication',
					'rest_framework.authentication.TokenAuthentication',
				)
				# drf的其他设置
			}
			

	-- step2 将rest_framework.authtoken添加到install_apps
	
		INSTALLED_APPS = (
			...
			'rest_framework.authtoken'
		)
		
	-- step3 配置url
		from rest_framework.authtoken import views
		urlpatterns += [
			url(r'^api-token-auth/', views.obtain_auth_token)
		]
		
	
	-- step4 获取token
		方式1： 通过post username, password到 api_token_auth url上，就会返回一个token
		
			-- obtain_auth_token会得到用户的一个token(如果用户之前没有token，会创建token然后返回）
		方式2：
			-- 当然也可以使用django的admin命令来得到用户的一个token 3.6.4drf版本
				python manage.py drf_create_token <username>
		方式3：
			-- 通过post_save信号，下面的这些代码必须是在
			
			from django.conf import settings
			from django.db.models.signals import post_save
			from django.dispatch import receiver
			from rest_framework.authtoken.models import Token

			@receiver(post_save, sender=settings.AUTH_USER_MODEL)
			def create_auth_token(sender, instance=None, created=False, **kwargs):
				if created:
					Token.objects.create(user=instance)
		
	-- step5 携带token到请求头字段：Authorization里面，然后访问一些需要用户认证的网页
	
		curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
		
	
		
	-- step6 认证后的结果
		将request里面user和auth分别填充
		request.user will be a Django User instance.否则会是annoyuser
		request.auth will be a rest_framework.authtoken.models.Token instance.
	
	
# drf自定制的用户验证：（忽略）
	from django.contrib.auth.models import User
	from rest_framework import authentication
	from rest_framework import exceptions

	class ExampleAuthentication(authentication.BaseAuthentication):
		def authenticate(self, request):
			username = request.META.get('X_USERNAME')
			if not username:
				return None

			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				raise exceptions.AuthenticationFailed('No such user')

			return (user, None)
	
	-- 用户验证后：，需要设置头字段X_USERNAME填充用户的名字
	
# 使用第三方包来进行用户验证
JSON Web Token Authentication

jwt:是一种基于token的用户验证机制，和内置的token验证机制不一样，jwt不需要用数据库存储token。
目前，有两个第三方的jwt包，可以使用。
djangorestframework-jwt  https://github.com/GetBlimp/django-rest-framework-jwt
 djangorestframework-simplejwt https://github.com/davesque/django-rest-framework-simplejwt
 
 # 为什么要使用jwt呢
 
 有两个原因: 一是drf内置的token是存储在数据库的。用户每发一个请求（需要验证的），都需要都数据库查询一次，如果用户量大的话，效率就会大大降低
			另外一个原因是：drf的token存储在数据库，如果是分布式的，每台服务器都需要到数据库服务器上面查询。 不适合单点登录的场景。