# django给我们提供的用户验证（登录时就要用到）

"""
有要求：
	authenticate进行验证，传入的参数必须是username,password，而且是关键字参数，
	auth之后还有执行django的Login函数，才是真正的登录了;
	
	为此，我们需要自定义一个验证， 

"""


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
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
            return render(request, "login.html", {'error': "用户名或密码错误"})
    else:
        return render(request, 'login.html')
		
		

		
# request提供了一个方法， 可以判断用户是否已经登录； 在前端由于我们已经传入了request, 可以调用其方法，不要带括号
request.user.is_authenticated():     #判断用户是否已登录

在前端就 {% if request.user.is_authenticated %}


{% if request.user.is_authenticated %}
	<div class="personal">
		<dl class="user fr">
			<dd>bobby<img class="down fr" src="/static/images/top_down.png"/></dd>
			<dt><img width="20" height="20" src="../media/image/2016/12/default_big_14.png"/></dt>
		</dl>
		<div class="userdetail">
			<dl>
				<dt><img width="80" height="80" src="../media/image/2016/12/default_big_14.png"/></dt>
				<dd>
					<h2>django</h2>
					<p>bobby</p>
				</dd>
			</dl>
			<div class="btn">
				<a class="personcenter fl" href="usercenter-info.html">进入个人中心</a>
				<a class="fr" href="/logout/">退出</a>
			</div>
		</div>
	</div>
{% else %}
	<a style="color:white" class="fr registerbtn" href="register.html">注册</a>
	<a style="color:white" class="fr loginbtn" href="/login/">登录</a>
{% endif %}
