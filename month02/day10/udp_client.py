"""
udp 客户端流程示例
重点代码　!!!
"""
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

# server_addr = ("192.168.1.255", 8889)
server_addr = ("127.0.0.1", 8888)

# 输入发送消息
while True:

    msg = input(">>")

    if not msg:
        break

    # 发送消息
    udp_socket.sendto(msg.encode(), server_addr)
    # 接受反馈
    data, addr = udp_socket.recvfrom(1024)
    print("from", addr, "receive", data.decode())

udp_socket.close()
