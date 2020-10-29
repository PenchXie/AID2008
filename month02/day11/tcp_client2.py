from socket import *

server_address = ("127.0.0.1", 45532)

while True:


    tcp_socket = socket(AF_INET, SOCK_STREAM)

    tcp_socket.connect(server_address)
    msg = input(">>")

    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)

    print(data.decode())
    tcp_socket.close()


