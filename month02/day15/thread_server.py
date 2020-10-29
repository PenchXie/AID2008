from socket import *
from threading import Thread


# 服务器地址
HOST = "0.0.0.0"
PORT = 45532
ADDR = (HOST, PORT)


# 实现具体的业务功能, 客户端请求都在这里处理
class MyThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
            self.connfd.send(b"Receive")
        self.connfd.close()


# 函数中编写并发服务
def main():
    sock = socket(AF_INET, SOCK_STREAM)  # tcp套接字
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d" % PORT)

    while True:
        # 循环接收客户端连接
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            # 退出服务
            sock.close()
            break
        # 使用自定义线程类为连接的客户端创建新线程
        t = MyThread(connfd)
        t.setDaemon(True) # 客户端随服务端退出
        t.start()

if __name__ == '__main__':
    main()