"""
tcp客户端　基础示例
重点代码　!!!
"""

from socket import *

# 服务器地址
# server_addr = ("127.0.0.1", 64646)
server_addr = ("127.0.0.1", 45532)
# server_addr = ('176.50.8.6', 8888)

# 创建tcp套接字
tcp_socket = socket()  # 使用默认参数

# 连接服务器
tcp_socket.connect(server_addr)

while True:
    # 收发消息
    msg = input(">>")

    # 客户端直接退出
    if not msg:
        break

    tcp_socket.send(msg.encode())
    # if msg == "##":  # 注意此循环位置, 客户端退出前应将退出信息发送给服务端
    #     break
    data = tcp_socket.recv(1024)
    print("Receive from server:", data.decode())

# 关闭套接字
tcp_socket.close()