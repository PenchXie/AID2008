"""
select IO 多路复用方法
"""
from select import select
from socket import *

f = open("my.log", 'a+')

sock_tcp = socket()
sock_tcp.bind(("0.0.0.0", 45532))
sock_tcp.listen(5)

sock_udp = socket(AF_INET, SOCK_DGRAM)


# 监控IO
print("开始监控IO")
rs, ws, xs = select([sock_tcp], [], [])
print("rlist", rs)
print("wlist", ws)
print("xlist", xs)