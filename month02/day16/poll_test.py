"""
poll IO 多路复用方法
"""
from select import *
from socket import *

f = open("my.log", 'a+')

sock_tcp = socket()
sock_tcp.bind(("0.0.0.0", 45532))
sock_tcp.listen(5)

sock_udp = socket(AF_INET, SOCK_DGRAM)

# 查找字典  需要与register的IO保持一致
map = {
    sock_tcp.fileno():sock_tcp,
    sock_udp.fileno():sock_udp,
    f.fileno(): f
}

# 监控IO
p = poll()  # 生成poll对象
p.register(sock_tcp, POLLIN | POLLERR)
p.register(sock_udp, POLLOUT)
p.register(f, POLLOUT)

print("开始监控IO")
events = p.poll()

# events --> [(fileno, event), ()]
# 必须获取到IO对象才能调用方法处理IO
# 创建查找字典  fileno-->IO object
print(events)
