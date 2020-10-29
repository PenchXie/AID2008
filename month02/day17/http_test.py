from socket import *

s = socket()
s.bind(("0.0.0.0", 64431))
s.listen()

c, addr = s.accept()
print("Connect from", addr)

# 接收浏览器发送的HTTP请求
data = c.recv(1024 * 10)
print(data.decode())

# 发送HTTP相应给浏览器
response = """HTTP/1.1 200 OK
Content-Type: text/html

Hello world\nhi
"""

c.send(response.encode())

c.close()
s.close()
