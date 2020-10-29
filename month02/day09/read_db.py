"""
数据库读
"""
import pymysql

# 生成数据库连接对象, 连接数据库
db_dict = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "fgo",
    "charset": "utf8"
}

db = pymysql.connect(**db_dict)

# 生成游标　游标：　操作数据库数据, 获取操作结果的对象
cur = db.cursor()

# 读取数据库内容
sql = "select name,age,score from masters where score>0;"
cur.execute(sql)
# for row in cur:
#     print(row)

# 获取一个查询记录
one = cur.fetchone()
print(one)

# 获取多个查询记录
many = cur.fetchmany(2)
print(many)

# 获取所有查询记录
total = cur.fetchall()
print(total)

# 关闭游标和数据库连接
cur.close()
db.close()