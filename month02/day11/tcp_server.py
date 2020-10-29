"""
tcp 服务端基础示例
重点代码　!!!
"""

from socket import *

# 创建tcp套接字　(不写参数默认也是tcp)
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定改地址
tcp_socket.bind(("0.0.0.0", 64646))

# 设置监听
tcp_socket.listen(5)

while True:
    # 等待客户端连接
    print("waiting for connection...")
    connfd, addr = tcp_socket.accept()
    print("connect to:", addr)

    while True:
        # 收发消息
        data = connfd.recv(1024)

        # 客户端退出, recv返回空字节串, 服务端也退出
        if not data:
            break

        # if data == b"##":
        #     break
        print("receive message:", data.decode())
        connfd.send(b"Get message")

    # 关闭套接字
    connfd.close()  # 断开连接

# tcp_socket.close()