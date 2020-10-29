"""
dict 客户端
"""
from socket import *

# 服务器
ADDR = ("0.0.0.0", 64433)


def do_history(sock, name):
    msg = "H %s" % name
    sock.send(msg.encode())  # 发送请求
    # 循环接收历史记录
    while True:
        data = sock.recv(1024).decode()
        if data == "##":
            break
        print(data)


# 第二界面
def second_phase(sock, name):
    while True:
        content = "======= 命令选项 =======\n"
        content += "\tQ: Query\n"
        content += "\tH: History\n"
        content += "\tE: Exit\n"
        content += "\t\tuser: %s" % name

        print(content)

        cmd = input("请输入命令:")
        # sock.send(cmd.encode())
        if cmd == "Q":
            do_query(sock, name)
        elif cmd == "H":
            do_history(sock, name)
        elif cmd == "E":
            break
        else:
            print("请输入正确命令")


def do_register(sock):
    while True:
        name = input("Username:")
        passwd = input("Passwd:")
        # 不允许用空格
        if " " in name or ' ' in passwd:
            print("用户名或密码不能有空格")
            continue

        msg = "R %s %s" % (name, passwd)
        sock.send(msg.encode())
        # 等待结果
        result = sock.recv(1024)
        if result == b"OK":
            print("注册成功")
            second_phase(sock, name)
        else:
            print("该用户已存在")
        return


def do_login(sock):
    name = input("Username:")
    passwd = input("Passwd:")
    msg = "L %s %s" % (name, passwd)
    sock.send(msg.encode())
    # 等待结果
    result = sock.recv(1024)
    if result == b"OK":
        # 进入登录界面
        second_phase(sock, name)
        pass
    else:
        print("用户名或密码错误")


def do_query(sock, name):
    while True:
        word = input("请输入要查询的单词:")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        sock.send(msg.encode())
        # 服务端无论是否查询到都返回要打印的内容
        result = sock.recv(1024).decode()
        print(result)


def main():
    # main启动服务
    sock = socket()
    sock.connect(ADDR)

    # 一级界面
    while True:
        content = "======= 命令选项 =======\n"
        content += "\tR: Register\n"
        content += "\tL: Login\n"
        content += "\tE: Exit\n"

        print(content)

        cmd = input("请输入命令:")
        # sock.send(cmd.encode())
        if cmd == "R":
            do_register(sock)
        elif cmd == "L":
            do_login(sock)
        elif cmd == "Q":
            do_query(sock)
        elif cmd == "E":
            sock.send(b"E")
            sock.close()
            break
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
