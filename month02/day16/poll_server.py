"""
基于epoll的 IO 网络并发模型
IO 多路复用与非阻塞搭配
"""

from select import *
from socket import *

# 网络地址
HOST = "0.0.0.0"
PORT = 45532
ADDR = (HOST, PORT)

# 创建监听套接字
sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

sockfd.setblocking(False)

map = {sockfd.fileno(): sockfd}

p = poll()
p.register(sockfd, POLLIN)

while True:

    events = p.poll()
    for tup in events:
        # if map[tup[0]] is sockfd:
        if tup[0] == sockfd.fileno():
            connfd, addr = map[tup[0]].accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            p.register(connfd, POLLIN)
            map[connfd.fileno()] = connfd
        else:
            data = map[tup[0]].recv(1024)
            if not data:
                p.unregister(tup[0]) # 不再关注
                map[tup[0]].close()
                del map[tup[0]]
                continue
            print(data.decode())
            map[tup[0]].send(b"OK")


