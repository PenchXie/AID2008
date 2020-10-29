from socket import *
from time import sleep, ctime

HOST = "0.0.0.0"
PORT = 1234
ADDR = (HOST, PORT)

sock = socket()
sock.bind(ADDR)
sock.listen(5)

# # 设置为非阻塞
# sock.setblocking(False)
# 设置超时等待
sock.settimeout(3)

# 打开日志文件
file = open("my.log", 'a')

while True:
    try:
        connfd, addr = sock.accept()
        print("Connect from", addr)
    except timeout as e:
        print("超时等待")
        msg = "%s : %s\n" % (ctime(), e)
        file.write(msg)
    except BlockingIOError as e:
        print("非阻塞日志")
        msg = "%s : %s\n" % (ctime(), e)
        file.write(msg)
        sleep(2)
    else:
        data = connfd.recv(1024)
        print(data.decode())