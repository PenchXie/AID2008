import time
from socket import *

# 创建tcp套接字　(不写参数默认也是tcp)
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定改地址
tcp_socket.bind(("0.0.0.0", 64646))

# 设置监听
tcp_socket.listen(5)

# 等待客户端连接
print("waiting for connection...")
connfd, addr = tcp_socket.accept()
print("connect to:", addr)

time_tuple = time.localtime()
filename = time.strftime("%Y-%m-%d", time_tuple) + ".jpg"
# filename = time.strftime("%Y-%m-%d", time_tuple) + ".txt"
file = open(filename, 'wb')

while True:
    # 收发消息
    data = connfd.recv(1024)
    # print("Receive:", data)
    # 客户端退出, recv返回空字节串, 服务端也退出
    # if not data:
    #     break

    if data == b"##":
        break

    file.write(data)
    # print("123")

connfd.send(b"Receive image")
file.close()

# 关闭套接字
connfd.close()  # 断开连接
tcp_socket.close()
