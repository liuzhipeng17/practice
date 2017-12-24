# form组件两个功能：
"""
	-1 生成html
	
	-2 对数据进行验证（格式，长度等）
"""

# 利用from来实现登录，验证数据的格式，以及提示错误信息

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
			
#
from django.forms import Form, fields


class LoginForm(Form):
    username = fields.CharField(required=True)
    password = fields.CharField(required=True, min_length=5, max_length=10)