import django
import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * From news"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result) # {'id': 1, 'title': '本机新闻标题'}
finally:
    connection.close()
