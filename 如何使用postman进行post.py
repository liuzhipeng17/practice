curl -X POST http://192.168.33.10:9000/v1/article/ -H 'ContentType: application/json' -d '{"source":"web python","title":"如何学习python web33","body":"首先，你要学会web的基础知识，web的网络安全，http等；其次，你要会python, 第三，你要会python的web框架","abstract":"如何学习python web","status":0,"author_id":17,"article_images": [{"image": "F:\\liu\\1111535000.jpg"} , {"image": "F:\\liu\\1111534999.jpg"}]}'


{
"source":"web python",
"title":"如何学习python web33",
"body":"首先，你要学会web的基础知识，web的网络安全，http等；其次，你要会python, 第三，你要会python的web框架",
"abstract":"如何学习python web",
"status":0,
"author_id":17,
"article_images": [{"image": "F:\\liu\\1111535000.jpg"} , {"image": "F:\\liu\\1111534999.jpg"}]
}


# step1 设置url 
	http://192.168.33.10:9000/jwt-auth/
	
# step2 填写body（选择raw--json(application)
	{
	"mobile":"15876684200",
	"password":"Lzhpeng17"
	}

# step3 获取token
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE1ODc2Njg0MjAwIiwibW9iaWxlIjoiMTU4NzY2ODQyMDAiLCJ1c2VyX2lkIjoxNywiZW1haWwiOiIiLCJleHAiOjE1MTUzMTQ5ODN9.qnTliVwgYDXG_V6evMRi6U7GePnetcxSUFFBvB2Huc0"
}

# step4 post数据(带上token)访问protect-url



	