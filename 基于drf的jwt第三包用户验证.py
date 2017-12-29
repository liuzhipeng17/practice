# 使用第三方包django-rest-framework-jwt进行用户验证：
	
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