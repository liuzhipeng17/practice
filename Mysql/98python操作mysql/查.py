import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="lzpdb", charset='utf8') # 连接数据库
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 当cursor=pymysql.cursors.DictCursor ，result结果会按字典返回
sql = "select uid from user where uname=%s"
cursor.execute(sql, 'alex')
result = cursor.fetchone() # 这里是查找所有记录fetall(); fetone()是按一条一条查
print(type(result), result)
cursor.close()
conn.close()

print(result)

