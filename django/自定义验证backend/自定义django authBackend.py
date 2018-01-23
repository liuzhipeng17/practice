# step1 自定义auth方法

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 对于那种唯一的，采用get来是非常好。超过1个，get就会报异常；
            if user.check_password(password): #传入的password是明文，调用check_password进行密文对比
                return user
        except Exception as e:
            return None
			

# login函数不用改变
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # 借用django的auth方法
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {'error': '用户名或密码错误')
    else:
        return render(request, 'login.html')
		

# 设置settings.py， 使得login里面的authenticate执行的是我们自定义CustomAuthBackend 里面的authenticate函数
AUTHENTICATION_BACKENDS = ('users.views.CustomAuthBackend',)