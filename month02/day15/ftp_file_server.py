"""
[1] 分为服务端和客户端，要求可以有多个客户端同时操作。
[2] 客户端可以查看服务器文件库中有什么文件。
[3] 客户端可以从文件库中下载文件到本地。
[4] 客户端可以上传一个本地文件到文件库。
[5] 使用print在客户端打印命令输入提示，引导操作
"""
import os
from signal import *
from socket import *
from threading import Thread
from time import sleep

HOST = "0.0.0.0"
PORT = 65321
ADDR = (HOST, PORT)

# 文件库位置
FTP = "/home/tarena/FTP/"


class FTPserver(Thread):
    def __init__(self, connfd: socket):
        self.connfd = connfd
        super().__init__()

    # 线程启动方法
    def run(self) -> None:
        while True:
            # 接收某一个客户端各类请求
            msg = self.connfd.recv(1024).decode()
            data = msg.split(" ")
            print(data)
            if data[0] == "LIST":
                self.do_list()
            elif data[0] == "UPLOAD":
                self.do_upload(data[1])
            elif data[0] == "DOWNLOAD":
                self.do_download(data[1])
            elif not data[0] or data == "EXIT":
                break
        self.connfd.close()

    # 处理请求文件列表
    def do_list(self):
        # 判断文件库是否为空
        files = os.listdir(FTP)
        if not files:
            self.connfd.send(b"FAIL")  # 失败
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            # 一次性发送所有文件名
            data = "\n".join(files)
            self.connfd.send(data.encode())
            sleep(0.1)
            self.connfd.send(b"##")

    def do_upload(self, filename: str):
        if os.path.exists(FTP + filename):
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            file = open(FTP + filename, 'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b"##":
                    break
                file.write(data)
            file.close()

    def do_download(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send(b"OK")
            file = open(FTP + filename, 'rb')
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            sleep(0.1)
            self.connfd.send(b"##")
            file.close()
        else:
            self.connfd.send(b"FAIL")


# 函数中搭建并发结构
def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d" % PORT)
    signal(SIGCHLD, SIG_IGN)  # 处理僵尸进程

    while True:
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            # 退出服务
            sock.close()
            break
        t = FTPserver(connfd)
        t.setDaemon(True)  # 客户端随服务端退出
        t.start()


if __name__ == '__main__':
    main()
