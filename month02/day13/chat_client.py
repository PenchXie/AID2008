"""
chat room 客户端代码
"""
import sys
from socket import *
from multiprocessing import Process
from time import sleep

# 服务器地址
# ADDR = ('127.0.0.1', 36942)
ADDR = ('119.3.124.77', 8000)

def login(sock):
    while True:
        # 进入聊天室
        name = input("Name:")
        # 发送姓名
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        # 接收结果
        result, addr = sock.recvfrom(128)
        if result.decode() == "OK":
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")




def send_msg(sock, name):
    while True:
        try:
            content = input("发言:")
        except KeyboardInterrupt:
            content = "exit"
        # 输入exit表示要退出聊天室
        if content == "exit":
            msg = "EXIT " + name
            sock.sendto(msg.encode(), ADDR)
            sys.exit("您已退出聊天室")

        msg = "CHAT %s %s" % (name, content)
        # 向服务器循环发送
        sock.sendto(msg.encode(), ADDR)


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        msg = "\n%s\n发言:" % data.decode()
        print(msg, end="")


# 网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0", 65521))
    sock.sendto(b"test....", ADDR)

    name = login(sock) # 进入聊天室

    # 创建子进程　用于接收消息
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True # 父进程退出子进程也退出
    p.start()
    send_msg(sock, name) # 父进程发送消息
    p.join()



    """
    客户端:
    1. input 姓名
    2. 向服务端发送姓名
    3. 等待服务端回复, 可以则进行下一步, 不行返回第一步
    服务端:
    1. 等待接收姓名
    2. 姓名不在已有列表中, 回复客户端可以进入, 否则回复客户端不能进入
    """

if __name__ == '__main__':
    main()