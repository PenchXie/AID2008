"""
web server 程序
完成一个类, 提供给使用者
可以通过这个类快速搭建服务
完成网页展示
"""
import re
from socket import *
from select import select


# 封装所有web后端功能
class WebServer():
    def __init__(self, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.create_socket()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    # 创建设置套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    # 绑定地址
    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    def handle(self, connfd):
        # http请求
        request = connfd.recv(1024 * 10).decode()
        # 使用正则表达式匹配请求内容
        pattern = r"[A-X]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)
        if request:
            # 提取请求内容
            info = result.group("info")
            print("请求内容:", info)

            self.send_html(connfd, info)
        else:
            # 匹配不到则退出
            return

    def send_html(self, connfd, info):
        try:
            if info == "/":
                info = "/index.html"
            file = open("./static" + info, 'rb')
        except:
            # 请求的网页不存在
            with open("./static/404.html", 'rb') as file:
                data = file.read()
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
        else:
            data = file.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += "Content-Length: %d\r\n" % len(data)
            response += "\r\n"
            file.close()
        finally:
            response = response.encode() + data
            connfd.send(response)


    # 启动整个服务
    def start(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        # 先监控监听套接字
        self.rlist.append(self.sock)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    connfd, addr = r.accept()
                    print("Connect from", addr)
                    connfd.setblocking(False)
                    self.rlist.append(connfd)  # 将客户端连接套接字也监控起来
                else:
                    # 某个浏览器发消息　connfd 就绪
                    self.handle(r)
                    self.rlist.remove(r)
                    r.close()


if __name__ == '__main__':
    # 需要用户决定: 地址 网页
    httpd = WebServer(
        host="0.0.0.0",
        port=65431,
        html="./static"
    )
    # 启动服务
    httpd.start()
