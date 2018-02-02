
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="db1", charset='utf8')
cursor = conn.cursor()
cursor.callproc('p3',(8,10))
result = cursor.fetchall()
cursor.close()
conn.close()
print(result)

# ((8, '男', 2, '李三'), (9, '男', 2, '李一'), (10, '女', 2, '李二'))