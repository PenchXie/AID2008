from socket import *

import pymysql

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(("0.0.0.0", 46721))

db_dict = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**db_dict)
# 生成游标
cur = db.cursor()

sql = "select mean from words where word=%s"

while True:
    # 接收单词
    word, addr = udp_socket.recvfrom(40)
    print("from", addr, "receive", word.decode())

    if not word:
        break
    cur.execute(sql, [word.decode()])
    explanation = cur.fetchone()[0]  # fetchone会返回一个元组
    print(explanation)

    # 发送解释
    n = udp_socket.sendto(explanation.encode(),addr)
    print("Send %d bytes" % n)
