# step1 install openJDK

	sudo apt-get update
	sudo apt-get install openjdk-7-jre

	# 检验openjdk是否安装成功
	java -version
	
# step2 install java8

	sudo add-apt-repository -y ppa:webupd8team/java

	sudo apt-get update

	sudo apt-get -y install oracle-java8-installer

	java -version
	
# step3  Downloading and Installing Elasticsearch

	wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.deb
	
	sudo dpkg -i elasticsearch-1.7.2.deb
	
	
# step3 设置开机自启动elasticsearch
	sudo update-rc.d elasticsearch defaults
	

# step4 configuring elastic

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
