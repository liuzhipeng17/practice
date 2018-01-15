vhttp://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

-# step1 创建虚拟环境：

	sudo pip install virtualenv virtualenvwrapper
	
	echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
	source ~/.bashrc
	
	mkvirtualenv firstsite
	
	
	# 上传本地开发包到虚拟环境：(可忽略）
		workon xxx
		pip freeze > requirements.txt
		拷贝该文件到firstsite里面
		pip install -r requirements.txt
		
		# mysql_config not found 问题
		sudo apt-get install libmysqlclient-dev
		pip install -r requirements.txt


-# step2 安装uwsgi(先在虚拟环境）
	sudo apt-get install python-dev  # ubuntu 或者debain
	workon fistsite
	pip install uwsgi
	
	
-# step3 测试uwsgi
	
	-- uwsgi 测试 django 工程(暂时不能访问静态文件）
		django-admin.py createproject firstsite
		
		cd fistsite
		
		./manage.py migrate
		
		uwsgi --http :8000 --module fistsite.wsgi
		
		# uwsgi --http :8080 --home /home/vagrant/.virtualenvs/firstsite --chdir /vagrant_data/firstsite -w firstsite.wsgi

		
		# 浏览器访问: 返回it worked, 说明下面的通道是成功的
		the web client <-> uWSGI <-> Django
	
	
	
-# step4 创建配置文件，来启动uwsgi
	# fistsite_uwsgi.ini
		# Django-related settings
		# the base directory (full path)
		chdir           = /vagrant_data/fistsite
		# Django's wsgi file
		module          = fistsite.wsgi
		# the virtualenv (full path)
		home            = /home/vagrant/.virtualenvs/firstsite  # 有些是virtualenv

		# process-related settings
		# master
		master          = true
		# maximum number of worker processes
		processes       = 10
		# the socket (use the full path to be safe
		socket          = 127.0.0.1:8001  #socket启动， 这个端口要和upstream django里面的一致
		# ... with appropriate permissions - may be needed
		chmod-socket    = 664
		# clear environment on exit
		vacuum          = true


-# step5 退出虚拟环境，在系统安装uwsgi, pip install uwsgi 


-# step6 Emeperor mode来启动uwsgi

	# step1 create a directory for the vassals
	sudo mkdir /etc/uwsgi
	sudo mkdir /etc/uwsgi/vassals

	sudo ln -s /path/to/your/mysite/mysite_uwsgi.ini /etc/uwsgi/vassals/
	
	# step2  run the emperor

	sudo uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data   # www-data是启动nginx的用户
	
	
	# 参数说明The options mean:

		emperor: where to look for vassals (config files)
		uid: the user id of the process once it’s started
		gid: the group id of the process once it’s started
		
-# step7 开机自启动uwsgi
	编辑/etc/rc.local
	
	在exit0 前面添加
	/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log
	
	
	
-# step8 安装nginx 

	sudo apt-get install nginx
	sudo /etc/init.d/nginx start    # start nginx
	
	# 测试nginx 
		浏览器访问: 127.0.0.1:80 如果返回nginx work 说明下面的通道是成功的:
			the web client <-> the web server（nginx)
		
		
-# step9 配置nginx

	-- step1 在fistsite工程内创建uwsgi_params ， 并添加以下内容：（连接在此）https://github.com/nginx/nginx/blob/master/conf/uwsgi_params
		# uwsgi_params
		uwsgi_param  QUERY_STRING       $query_string;
		uwsgi_param  REQUEST_METHOD     $request_method;
		uwsgi_param  CONTENT_TYPE       $content_type;
		uwsgi_param  CONTENT_LENGTH     $content_length;

		uwsgi_param  REQUEST_URI        $request_uri;
		uwsgi_param  PATH_INFO          $document_uri;
		uwsgi_param  DOCUMENT_ROOT      $document_root;
		uwsgi_param  SERVER_PROTOCOL    $server_protocol;
		uwsgi_param  REQUEST_SCHEME     $scheme;
		uwsgi_param  HTTPS              $https if_not_empty;

		uwsgi_param  REMOTE_ADDR        $remote_addr;
		uwsgi_param  REMOTE_PORT        $remote_port;
		uwsgi_param  SERVER_PORT        $server_port;
		uwsgi_param  SERVER_NAME        $server_name;
	
	-- step2 创建fistsite_nginx.conf， 并添加以下内容:
		# mysite_nginx.conf

		# the upstream component nginx needs to connect to
		upstream django {
			# server unix:///path/to/your/mysite/mysite.sock; # for a file socket
			server 127.0.0.1:8001; # for a web port socket (we'll use this first)
		}

		# configuration of the server
		server {
			# the port your site will be served on
			listen      8000;
			# the domain name it will serve for
			server_name 192.168.33.10; # substitute your machine's IP address or FQDN
			#server_name 192.168.33.10 www.test.com; # substitute your machine's IP address or FQDN

			charset     utf-8;

			# max upload size
			client_max_body_size 75M;   # adjust to taste

			# Django media
			location /media  {
				alias /vagrant_data/fistsite/media;  # your Django project's media files - amend as required, 在工程fistsite内，手动创建media
			}

			location /static {
				alias /vagrant_data/fistsite/static; # your Django project's static files - amend as required，
			}
			

			# Finally, send all non-media requests to the Django server.
			location / {
				uwsgi_pass  django;
				include     /vagrant_data/fistsite/uwsgi_params; # the uwsgi_params file you installed
			}
		}
		
	-- step3 
		sudo ln -s ~/path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/
	
	
--# step10 修改settings.py
	-- settings.py 添加
	STATIC_ROOT = os.path.join(BASE_DIR, "static/")
	
	同时要注释掉STATICFILES_DIRS
	-- 执行命令
	./manage.py collectstatic  # 会将文件拷贝到static目录
	
	-- 测试nginx 是否能访问静态文件
		# step1
		将一个图片test.jpg放到media目录内或者static内
		
		# step2 启动nginx(
		/etc/init.d/nginx restart  # ps -aux |grep nginx ； pkill -f nginx
		
		# step3 浏览器访问http://127.0.0.1:8000/media/test.jpg
					http://127.0.0.1:8000/static/test.jpg
					
	-- debug改成false
			DEBUG=False

	 
- # step11 有时候经常是gatway 502 问题--一般是uwsgi的问题


-# step12 网站打不开，一般是nginx的问题

	# nginx -t 查看是什么问题或者 sudo tail -f /var/log/nginx/error.log
	
-# step13 /run/nginx.pid 找不到， 
	sudo nginx -c /etc/nginx/nginx.conf 

	sudo nginx -s reload
	
	sudo nginx -t 
	

