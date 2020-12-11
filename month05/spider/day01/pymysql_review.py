import pymysql

# 1 连接对象 游标对象
dict01 = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'noveldb',
    'charset': 'utf8'
}
# 'localhost', 'root', '123456', 'noveldb', charset='utf8'
db = pymysql.connect('localhost', 'root', '123456', 'noveldb', charset='utf8')
cur = db.cursor()
#
# 2 执行sql命令
ins = 'insert into novel_tab values(%s,%s,%s,%s);'
cur.execute(ins, ['战神', 'zh.com', '黑龙', '真厉害'])

# 提交到数据库执行
db.commit()

# 关闭
cur.close()
db.close()