
# 使用第三方包django-rest-framework-jwt进行用户验证：

 # 为什么要使用jwt来进行验证
 
	首先是drf内置的token验证存在不足: 一是drf内置的token是存储在数据库的。用户每发一个请求（需要验证的），都需要都数据库查询一次，如果用户量大的话，效率就会大大降低
			另外一个原因是：drf的token存储在数据库，如果是分布式的，每台服务器都需要到数据库服务器上面查询。 不适合单点登录的场景。
			
	
	二是：jwt:是一种基于token的用户验证机制，和内置的token验证机制不一样，jwt不需要用数据库存储token。
		
 # 目前，支持django rest-framework 的jwt第三方包：
	目前，有两个第三方的jwt包，可以使用。
		djangorestframework-jwt  https://github.com/GetBlimp/django-rest-framework-jwt
		djangorestframework-simplejwt https://github.com/davesque/django-rest-framework-simplejwt
	
# 安装：
	pip install django-rest-framework
    pip install djangorestframework-jwt
	
# 和drf的token配置一样，配置settings.py里面的验证机制： 将JSONWebTokenAuthentication添加到DEFAULT_AUTHENTICATION_CLASSES
	REST_FRAMEWORK = {
		'DEFAULT_PERMISSION_CLASSES': (
			'rest_framework.permissions.IsAuthenticated',
		),
		'DEFAULT_AUTHENTICATION_CLASSES': (
			'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
			'rest_framework.authentication.SessionAuthentication',
			'rest_framework.authentication.BasicAuthentication',
		),
	}

	
# 设置一个url，通过post用户的username和password就能获取用户的token
	from rest_framework_jwt.views import obtain_jwt_token
	#...

	urlpatterns = [
		'',
		# ...

		url(r'^api-token-auth/', obtain_jwt_token),
	]
		


# 创建用户： username: admin, password: admin123


# 通过命令curl测试：
	$ curl -X POST -d "username=admin&password=password123" http://localhost:8000/api-token-auth/
	或者这样
	$ curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"password123"}' http://localhost:8000/api-token-auth/

# 然后就可以携带这个token，去访问一些需要用户验证的网页了
	$ curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/


# 