"""
套接字使用基础示例
"""
import socket

# 创建一个UDP套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

udp_socket.bind(("176.50.8.4",23876))
