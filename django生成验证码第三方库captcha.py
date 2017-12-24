# 使用第三方库captcha实现验证码

#  step1 安装以及集成captcha到django   
"""
	http://django-simple-captcha.readthedocs.io/en/latest/usage.html
	
	step1: pip install  django-simple-captcha==0.5.6
	
	step2:  INSTALLED_APPS里面添加应用 'captcha' 
	
	step3: 生成captcha需要的数据库  python manage.py makemigrations     migrate
	
	step4:

	urlpatterns += [
		url(r'^captcha/', include('captcha.urls')),
	]
 

 执行完migrate ，数据库增加了一个表：captcha_captchastore
 
	challenge = models.CharField(blank=False, max_length=32) # 验证码大写或者数学计算比如 1+1
	response = models.CharField(blank=False, max_length=32)  # 需要输入的验证码 验证码小写或数学计算的结果 比如 2
	hashkey = models.CharField(blank=False, max_length=40, unique=True) # hash值
	expiration = models.DateTimeField(blank=False) # 到期时间

"""


# step2: 生成form， 我是注册
from django.forms import Form, fields
from captcha.fields import CaptchaField


class RegisterForm(Form):
    email = fields.EmailField(required=True)
    password = fields.CharField(required=True, min_length=5, max_length=10)
    captcha = CaptchaField(error_messages={'invalid': u"验证码输入错误"})
	

# step3利用form组件生成Html

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    def post(self, request):
        pass
		
# step4 template 设置
 
 {{ register_form.captcha }} 
 """
 上面的等效生成下面的三个标签； 第一个就是图片， 第二个就是隐藏的hash，第三个就是你要输入的验证码；
 
 根据hash值 和你输入的验证码 到数据库captcha_captchastore 查询
 """
{#<img src="/captcha/image/2f3f82e5f7a054bf5caa93b9b0bb6cc308fb7011/" alt="captcha" class="captcha" /> #}
{#<input id="id_captcha_0" name="captcha_0" type="hidden" value="2f3f82e5f7a054bf5caa93b9b0bb6cc308fb7011" /> #}
{#<input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" />#}


# 点击图片，刷新验证码

"""
打开captcha源码中的url可以看到

urlpatterns = [
    url(r'image/(?P<key>\w+)/$', views.captcha_image, name='captcha-image', kwargs={'scale': 1}),
    url(r'image/(?P<key>\w+)@2/$', views.captcha_image, name='captcha-image-2x', kwargs={'scale': 2}),
    url(r'audio/(?P<key>\w+).wav$', views.captcha_audio, name='captcha-audio'),
    url(r'refresh/$', views.captcha_refresh, name='captcha-refresh'),
]

调到captcha_refresh可以看到： 通过ajax发送请求过来刷新。 返回的数据是json数据
def captcha_refresh(request):
    """  Return json with new captcha for ajax refresh request """
    if not request.is_ajax():
        raise Http404

    new_key = CaptchaStore.pick()
    to_json_response = {
        'key': new_key,
        'image_url': captcha_image_url(new_key),
        'audio_url': captcha_audio_url(new_key) if settings.CAPTCHA_FLITE_PATH else None
    }
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')
	
	
# 我们将获取到的key和image_url更新到以下两个标签
{#<img src="/captcha/image/2f3f82e5f7a054bf5caa93b9b0bb6cc308fb7011/" alt="captcha" class="captcha" /> #}
{#<input id="id_captcha_0" name="captcha_0" type="hidden" value="2f3f82e5f7a054bf5caa93b9b0bb6cc308fb7011" /> #}

"""


function refresh_captcha(event){
    $.get("/captcha/refresh/?"+Math.random(), function(result){
        $('#'+event.data.form_id+' .captcha').attr("src",result.image_url);
        $('#id_captcha_0').attr("value",result.key);
    });
    return false;
}


# 比较简单的一个版本
# ajax 刷新
 $('.captcha').click(function(){
        console.log('click');
         $.getJSON("/captcha/refresh/",
                  function(result){
             $('.captcha').attr('src', result['image_url']);
             $('#id_captcha_0').val(result['key'])
          });


});