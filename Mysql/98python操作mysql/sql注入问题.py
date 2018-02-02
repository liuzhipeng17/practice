import pymysql

user = input("username:").strip()
pwd = input("password:").strip()

conn = pymysql.connect(host="localhost", user="root", password="", database="db2") # 连接数据库
cursor = conn.cursor()
sql = "select * from userinfo where username=%s and password=%s" %(user,pwd)
print(sql)
cursor.execute(sql)
result = cursor.fetchone()
cursor.close()
conn.close()

print(result)
if result:
    print("登录成功")
else:
    print("登录失败")

# userinfo表里面根本没有uuu or 1=1 --这个用户，为什么能登录成功呢？
# select * from userinfo where username='uuu' or 1=1 -- and password='123'
# 可以看到我们的sql语句是where条件永远成立， and后面部分被注释掉
# 黑客经常用这招来黑掉网站，所以一定不要自己拼接sql语句，而是用execute 传参数

# username:'uuu' or 1=1 --
# password:'123'
# select * from userinfo where username='uuu' or 1=1 -- and password='123'
# (1, 'alex', '123')
# 登录成功