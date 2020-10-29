import re

import pymysql

file = open('dict.txt', 'r')
word_list = []
for line in file.readlines():
    # print(re.findall('(\S+) +(.+)', line))
    # word_list += re.findall('(\S+)\s+(.+)', line)
    temp_list = re.findall('(\S+)\s+(.*)', line)
    if len(temp_list[0][0]) > 20:
        print(temp_list)
    word_list.append(temp_list[0])

# print(word_list)
db_dict = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}

db = pymysql.connect(**db_dict)

cur = db.cursor()

try:
    sql = "insert into words (word,mean) values (%s,%s);"
    cur.executemany(sql,word_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

file.close()
cur.close()
db.close()