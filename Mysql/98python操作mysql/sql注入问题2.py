import pymysql

user = input("username:").strip()
pwd = input("password:").strip()

conn = pymysql.connect(host="localhost", user="root", password="", database="db2") # 连接数据库
cursor = conn.cursor()
sql = "select * from userinfo where username='%s' and password='%s'" %(user,pwd)
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

# 当输入为 uuu ' or 1=1 -- \是也会登录成功
# username:uuu' or 1=1 -- \
# password:123
# select * from userinfo where username='uuu' or 1=1 -- \' and password='123'
# (1, 'alex', '123')
# 登录成功
