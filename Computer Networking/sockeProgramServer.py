from socket import *

host = "192.168.0.5"
port = 8000

s = socket(AF_INET , SOCK_STREAM)
s.bind((host , port))

s.listen(1)
print('Waiting to connect...')

clint_socket , addr = s.accept()

print('Connected')


msg = "Hello i am server"
data = msg.encode()
clint_socket.send(data)


data = clint_socket.recv(50)
msg = data .decode()
print(msg)


s.close()

