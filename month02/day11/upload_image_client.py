from socket import *

# 服务器地址
server_addr = ("127.0.0.1", 64646)
# server_addr = ('176.50.8.6', 8888)

# 创建tcp套接字
tcp_socket = socket()  # 使用默认参数

# 连接服务器
tcp_socket.connect(server_addr)

# with open('./timg.jpeg', 'rb') as f:
file = open('./timg.jpeg', 'rb')
# file = open('1.txt', 'rb')
for line in file.readlines():
    # print(line)

    tcp_socket.send(line)
file.close()

tcp_socket.send(b"##")
data = tcp_socket.recv(1024)
print("From server:", data.decode())

# 关闭套接字
tcp_socket.close()