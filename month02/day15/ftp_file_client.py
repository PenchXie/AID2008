"""
ftp 文件服务　客户端
c / s 连接 发请求 获取结果
"""
import sys
from socket import *

# 服务端地址
from time import sleep

ADDR = ("127.0.0.1", 65321)


# 发起请求的所有功能
class FTPClient():
    def __init__(self, sock: socket):
        self.sock = sock

    # 请求文件列表
    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        result = self.sock.recv(1024).decode()  # 等待回复
        # 根据不同结果分情况处理
        if result == "OK":
            # 接收文件列表
            while True:
                file = self.sock.recv(1024).decode()
                if file == "##":
                    break
                print(file)
        else:
            print("文件库为空")

    # 退出
    def do_exit(self):
        self.sock.send(b"EXIT")
        self.sock.close()
        sys.exit("谢谢使用")

    def do_upload(self):
        filepath = input("请输入要上传的文件路径:")
        try:
            file = open(filepath, 'rb')
        except:
            print("文件不存在或路径错误")
            return
        msg = "UPLOAD " + filepath.split("/")[-1]
        self.sock.send(msg.encode())
        result = self.sock.recv(1024)
        if result == b"OK":
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.sock.send(data)
            sleep(0.1)
            self.sock.send(b"##")
            file.close()
        else:
            print("文件已存在, 无法上传")

    def do_download(self):
        filename = input("请输入要下载的文件名:")
        msg = "DOWNLOAD " + filename
        self.sock.send(msg.encode())
        result = self.sock.recv(1024)
        if result == b"OK":
            file = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                file.write(data)
            file.close()


# 启动函数
def main():
    sock = socket()
    sock.connect(ADDR)

    ftp = FTPClient(sock)  # 实例化对象用于调用方法

    while True:
        print("""
        ======= 命令选项 =======
                 list
               download
                upload
                 exit
        """)
        cmd = input("请输入命令:")
        sock.send(cmd.encode())
        if cmd == "list":
            ftp.do_list()
        elif cmd == "exit":
            ftp.do_exit()
        elif cmd == "upload":
            ftp.do_upload()
        elif cmd == "download":
            ftp.do_download()
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
