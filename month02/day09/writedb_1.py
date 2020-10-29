"""
数据库写操作示例
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

# 写操作示例
name = input("Master_name:")
try:
    # sql = f"update masters set score=100 where name='{name}'"
    # cur.execute(sql)
    sql = "update masters set score=%s where name=%s"
    cur.execute(sql, [100, name])
    db.commit()  # 事物提交
except Exception as e:
    print(e)
    db.rollback()  # 事物回滚

# 关闭游标和数据库连接
cur.close()
db.close()
