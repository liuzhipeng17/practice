# step1 编写生成验证码脚本

	# -*- coding: utf-8 -*-
	import random
	from django.core.cache import cache
	
	
	random_code_fun =  lambda x : ''.join(random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqXxYyZz0123456789', x))
	print random_code_fun(5)

		
# step2 如何在django发送email
	

	EMAIL_HOST = 'smtp.sina.cn'  # 这个是你邮箱的服务器（一般在设置，客户端pop/imap/smtp里面，而且要打开stmp服务）
	EMAIL_HOST_USER = 'liucpliu@sina.cn'
	EMAIL_HOST_PASSWORD = 'xxxxxx'
	#DEFAULT_FROM_EMAIL = 'abc@domain.com'
	#SERVER_EMAIL = 'abc@domain.com'
	EMAIL_PORT = 25
	EMAIL_USE_TLS = False
	

# step3 python manage.py shell

	from django.core.mail import EmailMessage
	email = EmailMessage('Subject', 'Body', from_email="liucpliu@sina.cn", to=['def@domain.com'])
	email.send()
	
	# EmailMessage里面的第一个参是主题，第二个是内容，第三个是接收人（多个）
	

# step4 自定义注册验证码



