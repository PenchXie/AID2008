import pymysql

db_dict = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}

class DictDatabase():
    def __init__(self):
        self.db = pymysql.connect(**db_dict)

    def create_cursor(self):
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def register(self, name: str, passwd: str):
        sql = "select name from user where name=%s;"
        self.cur.execute(sql, [name])
        if self.cur.fetchone():
            return False

        sql = "insert into user (name, passwd) values (%s, %s);"
        self.cur.execute(sql, [name, passwd])
        self.db.commit()
        return True

    def login(self, name, passwd):
        # 加binary可区分大小写
        sql = "select name, passwd from user where binary name=%s and binary passwd=%s;"
        self.cur.execute(sql, [name, passwd])
        if self.cur.fetchone():
            return True
        return False

    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        return self.cur.fetchone()

    def insert_history(self, name, word):
        sql = "insert into history (word, user_id) values (%s, (select id from user where name=%s));"
        self.cur.execute(sql, [word, name])
        self.db.commit()

    def history(self, name):
        sql = "select name, word, time " \
              "from history left join user " \
              "on user_id=id where name=%s " \
              "order by time limit 10;"
        self.cur.execute()
        # ((name,word,time), (), ...)
        return self.cur.fetchall()



