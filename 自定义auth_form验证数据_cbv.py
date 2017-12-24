
# step1 自定义authbackend, 实现邮箱或者用户名登录
"""
1 settings.py要设置

2 自定义类; 类继承django.contrib.auth.backends.ModelBackend, 并重写quthenticate函数

3 利用django.db 的	Q进行或判断

"""

#settings.py设置
AUTHENTICATION_BACKENDS = ('users.views.CustomAuthBackend',)


from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 对于那种唯一的，采用get来是非常好。超过1个，get就会报异常；
            if user.check_password(password): #传入的password是明文，调用check_password进行密文对比
                return user
        except Exception as e:
            return None

# step2 form组件两个功能：
"""
	-1 生成html
	
	-2 对数据进行验证（格式，长度等）
"""

# forms.py
from django.forms import Form, fields


class LoginForm(Form):
    username = fields.CharField(required=True)
    password = fields.CharField(required=True, min_length=5, max_length=10)


# step3利用from来实现登录，验证数据的格式，以及提示错误信息: 

from django.views.generic.base import View
from .forms import LoginForm

			
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {'error': "用户名或密码错误"})
        else:
            return render(request, "login.html", {'login_form': login_form})
			
# step cbv的 url设置
"""
视图要继承from django.views.generic.base import View
"""
    url(r'^login/$', views.LoginView.as_view(), name="login"),
