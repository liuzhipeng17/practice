
# 使用第三方包django-rest-framework-jwt进行用户验证：

 # 为什么要使用jwt来进行验证
 
	首先是drf内置的token验证存在不足: 
			一是drf内置的token是存储在数据库的。用户每发一个请求（需要验证的），都需要都数据库查询一次，如果用户量大的话，效率就会大大降低
			另外一个原因是：drf的token存储在数据库，如果是分布式的，每台服务器都需要到数据库服务器上面查询。 不适合单点登录的场景。
			
	
	二是：jwt:是一种基于token的用户验证机制，和内置的token验证机制不一样，jwt不需要用数据库存储token。
			
		  服务器不需要保存jwt，
		
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
		), # 最好不要在这添加权限，这里是全局权限，如果是未鉴权用户，就访问不了
		'DEFAULT_AUTHENTICATION_CLASSES': (
			'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
			'rest_framework.authentication.SessionAuthentication',
			'rest_framework.authentication.BasicAuthentication',
		),
		# 这个authentication也最好不要做全局设置？
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


# jwt的验证原理
JWT是Auth0提出的通过对JSON进行加密签名来实现授权验证的方案，编码之后的JWT看起来是这样的一串字符：

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
由.分为三段，通过解码可以得到：

// 1. Headers
// 包括类别（typ）、加密算法（alg）；
{
  "alg": "HS256",
  "typ": "JWT"
}
// 2. Claims
// 包括需要传递的用户信息；
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
// 3. Signature
// 根据alg算法与私有秘钥进行加密得到的签名字串；
// 这一段是最重要的敏感信息，只能在服务端解密；
HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    SECREATE_KEY
)
在使用过程中，服务端通过用户登录验证之后，将Header+Claim信息加密后得到第三段签名，然后将签名返回给客户端，
在后续请求中，服务端只需要对用户请求中包含的JWT进行解码，即可验证是否可以授权用户获取相应信息