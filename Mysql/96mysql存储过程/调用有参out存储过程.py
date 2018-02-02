
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="db1", charset='utf8')
cursor = conn.cursor()
v = 0
cursor.callproc('p2',(10,'v')) # 还是传两个参数
r1 = cursor.fetchall()
print(r1)  # 打印执行存储过程的结果

sql = 'select @_p2_0,@_p2_1'   # @_p2_0代表第一个参数
cursor.execute(sql)  # 执行sql语句
r2 = cursor.fetchall() # 拿到上面查询的结果
print(r2)

cursor.close()
conn.close()


# ((8, '男', 2, '李三'), (9, '男', 2, '李一'), (10, '女', 2, '李二'))