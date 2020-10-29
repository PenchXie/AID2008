from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(("0.0.0.0", 34567))

tcp_socket.listen(5)

reply_dict = {}
with open('./1.txt', 'r') as f:
    for line in f.readlines():
        temp_list = line.split(" ")
        print(temp_list)
        reply_dict[temp_list[0]] = temp_list[-1]

while True:
    print("Waitng connection...")
    connfd, addr = tcp_socket.accept()
    print("connect to:", addr)

    data = connfd.recv(1024)

    for key in reply_dict:
        if data.decode() in key:
            response = reply_dict[key].encode()
            # tcp_socket.send(reply_dict[key].encode())
            print("a")
            break
    else:
        response = b"I don't know"
        # tcp_socket.send(b"I don't know")
        print("b")

    connfd.send(response)
    connfd.close()
