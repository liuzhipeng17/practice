# -*- coding: utf-8 -*-

# cookie 
"""
	-- 定义: 1 cookie是浏览器的一种本地存储机制。 浏览器将信息按键值对存储在cookie中，存储一些有用信息，比如用户的用户名， 密码, 可以存储服务器返回的任何东西
	
			 2 这些键值对是保存在不同的域名下， 不同的域名都有自己的键值对。 是不能跨域的
			 
			 3 浏览器在发送请求的时候，就会对应域名下的cookie发送给服务器。
			 
			 4 服务器就可以根据这些信息来获取
			 
	
	-- 利用cookie进行识别用户

 			浏览器登录请求，用户A登录-->服务器接收；

			浏览器<-----服务器发现浏览器的请求没有携带cookie， 就会传cookie给浏览器 ，此时cookie存储的用户的一些基本信息 
			  
						假设服务器返回用户的id, 浏览器保存id在cookie中，注意cookie是分服务器的， 不能跨域；
  
  
			浏览器用户A再发送请求，携带cookie--->服务器获取id, 获取id=1的用户信息； 这样就知道是用户A
  
  
		# id =1 只是为了方便描述，在浏览器中cookie保留的值，肯定不是明文的。

  
	-- cookie的危险：
	   用户的密码，用户名等信息是存储在浏览器上的， 如果有人获取浏览器的信息，就可以解码获取了信息。危险。
	   
	
	
	-- 解决方法（session)
	   -- 简单来说：就是根据用户的信息生成了一个随机字符串session_key，然后返回给浏览器的是这个字符串，而不是用户的信息
		  而在数据库中，将用户的信息session_data和session_key绑定。 服务器可以根据这个session_key得到用户的信息。
		  但是这个session_key是由期限的session_expire
	

"""


# session

"""
	session是保存在服务器中的，发送给用户的是session_id， 而不是用户的信息了。
	浏览器接收到session_id后，将其保存在cookie中。
	
	发送请求的时候，就会将这个session_id也一起发送给服务器。
	
	
	django的session， 默认是保存在数据库表django_session表中，
	   django session表有三个字段：
				session_key，
				session_data, 
				session_expire,
"""