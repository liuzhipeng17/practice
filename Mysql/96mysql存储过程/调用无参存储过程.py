
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="db1", charset='utf8')
cursor = conn.cursor()
cursor.callproc('p1')
conn.commit()
result = cursor.fetchall()
cursor.close()
conn.close()
print(result)

# ((1, '张磊老师'), (2, '李平老师'), (3, '刘海燕老师'), (4, '朱云海老师'), (5, '李杰老师'))