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
# 将图片存入数据库
with open('timg.jpeg', 'rb') as f:
    data = f.read()

try:
    sql = "update servants set image=%s;"
    cur.execute(sql, [data])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()