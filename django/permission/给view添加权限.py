# 根据django restframe work jwt进行用户验证

# 安装：
	pip install django-rest-framework
    pip install djangorestframework-jwt

# settings设置auth, 
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),# do not add permission here, at view add
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


# 设置url
	from rest_framework_jwt.views import obtain_jwt_token
	#...

	urlpatterns = [
		'',
		# ...

		url(r'^api-token-auth/', obtain_jwt_token),
	]
	
# 然后再没view添加perimission
#http://www.django-rest-framework.org/api-guide/permissions/


from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)  # 为鉴权用户只能read

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)