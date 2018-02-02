import pymysql

user = input("username:").strip()
pwd = input("password:").strip()

conn = pymysql.connect(host="localhost", user="root", password="", database="db2") # 连接数据库
cursor = conn.cursor() # 操作数据库是交由cursor来操作
# sql = "select * from userinfo where username='%s' and password='%s'" %(user,pwd)
# 不要自己拼接sql语句，而是用execute里面的参数传占位符
sql = "select * from userinfo where username=%s and password=%s"
# 传参要用元组，或者字典，或者list
cursor.execute(sql, (user, pwd))
result = cursor.fetchone()
cursor.close()
conn.close()

print(result)
if result:
    print("登录成功")
else:
    print("登录失败")
