"""
dict 服务端
* 接收请求
* 逻辑处理
* 将数据整合给客户端
"""
import sys
from multiprocessing import Process
from socket import *
from signal import *
from time import sleep

from dict_db import DictDatabase


class OnlineDictionary():
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(("0.0.0.0", 64433))
        self.sock.listen(5)
        self.db = DictDatabase()

    def handle(self, connfd: socket):
        self.db.create_cursor()
        while True:
            data = connfd.recv(1024).decode()
            tmp = data.split(" ")
            # L登录
            if tmp[0] == "L":
                self.do_login(connfd, tmp[1], tmp[2])
            # R注册
            elif tmp[0] == "R":
                self.do_register(connfd, tmp[1], tmp[2])
            # Q查单词
            elif tmp[0] == "Q":
                self.do_query(connfd, tmp[1], tmp[2])
            # H查历史记录
            elif tmp[0] == "H":
                self.do_history(connfd, tmp[1])
            else:
                # 退出
                break

        self.db.cur.close()
        self.db.close()
        connfd.close()

    def main(self):
        while True:
            try:
                connfd, addr = self.sock.accept()
                print("Connect from", addr)
            except KeyboardInterrupt:
                sys.exit()
            signal(SIGCHLD, SIG_IGN)
            p = Process(target=self.handle, args=(connfd,))
            p.daemon = True
            p.start()

    def do_login(self, connfd: socket, name: str, passwd: str):
        if self.db.login(name, passwd):
            connfd.send(b"OK")
        else:
            connfd.send(b"FAIL")


    def do_register(self, connfd, name, passwd):
        if self.db.register(name, passwd):
            connfd.send(b"OK")
        else:
            connfd.send(b"FAIL")

    def do_query(self, connfd, name, word):
        # 返回单词解释
        mean = self.db.query(word)
        if mean:
            mean = mean[0]
        else:
            mean = "Not Found"
        connfd.send(mean.encode())
        self.db.insert_history(name, word)

    def do_history(self, connfd, name):
        result = self.db.history(name)
        for row in result:
            msg = "%s\t%s\t%s\n" % row
            connfd.send(msg.encode())
        sleep(0.1)
        connfd.send(b"##")


if __name__ == '__main__':
    od = OnlineDictionary()
    od.main()
