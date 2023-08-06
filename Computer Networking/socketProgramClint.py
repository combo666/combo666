from socket import *

server_host = "192.168.0.5"
server_port = 8000

server_socket = socket(AF_INET , SOCK_STREAM)
server_socket.connect((server_host , server_port))


data = server_socket.recv(50)
msg = data.decode()
print(msg)


msg = "hello i am clint"
data = msg.encode()
server_socket.send(data)


server_socket.close()
