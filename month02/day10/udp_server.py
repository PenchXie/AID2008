"""
udp 服务端基础功能示例

重点代码　!!!
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0", 8888))

while True:
    # 接受消息
    data, addr = udp_socket.recvfrom(1024)
    print("from", addr, "receive:", data.decode())

    # 发送消息
    n = udp_socket.sendto(b"Get", addr)
    print("Send%d bytes"%n)

# 关闭套接字
# udp_socket.close()