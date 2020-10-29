import re
from socket import *

s = socket()
s.bind(("0.0.0.0", 64432))
s.listen()

c, addr = s.accept()
print("Connect from", addr)

# 接收浏览器发送的HTTP请求
data = c.recv(1024 * 10).decode()
print(data)
content = re.findall(r"GET (.+?) .*", data, flags=re.DOTALL)[0]
# print(content)
if content == "/python":
    file = open('Welcome to Python.org.html', 'r')
    html = file.read()
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n"
    response += "\r\n"
    response += html
    file.close()
else:
    response = """HTTP/1.1 404 Not Found
Content-Type: text/html

ERROR 404 Not Found
    """

# 发送HTTP相应给浏览器
c.send(response.encode())

c.close()
s.close()