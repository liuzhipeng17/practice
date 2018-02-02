import pymysql

# 增加单条记录（写死）
# conn = pymysql.connect(host="localhost", user="root", password="", database="db2") # 连接数据库
# cursor = conn.cursor() # 操作数据库是交由cursor来操作
# sql = "insert into userinfo(username, password) values('lzp','123')"
# cursor.execute(sql)
# conn.commit()
# # 要提交事务，不然不会生效到数据库；当修改数据库值要commit
# cursor.close()
# conn.close()

# 增加单条记录（变量）
# conn = pymysql.connect(host="localhost", user="root", password="", database="db2") # 连接数据库
# cursor = conn.cursor() # 操作数据库是交由cursor来操作
# user = 'egon'
# pwd = '123'
# sql = "insert into userinfo(username, password) values(%s,%s)"
# cursor.execute(sql,(user,pwd))
# conn.commit()
# # 要提交事务，不然不会生效到数据库；当修改数据库值要commit
# cursor.close()
# conn.close()

# 批量增加多条记录
conn = pymysql.connect(host="localhost", user="root", password="", database="db2") # 连接数据库
cursor = conn.cursor() # 操作数据库是交由cursor来操作
sql = "insert into userinfo(username, password) values(%s,%s)"
# 注意sql注入问题 --
# 如果是自己拼接sql，会导致sql 注入问题， 比如我输入
r = cursor.executemany(sql, [('wpeqi', '123'),('laoyao', '123')])   # 这样防止sql注入
# r为受影响的行数
conn.commit()
# 获取新增数据的id
print(cursor.lastrowid)
# 要提交事务，不然不会生效到数据库；当修改数据库值要commit
cursor.close()
conn.close()


