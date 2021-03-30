import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Client socket created')

c.connect(('localhost', 9999))

name = input('Enter your name')
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())