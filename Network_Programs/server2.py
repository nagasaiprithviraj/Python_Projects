
import socket
print(type(socket.gethostbyname(socket.gethostname())))

c = socket.socket()

c.connect(('192.168.1.142', 9999))
num1 = input("Enter your number")
c.send(bytes(num1,'utf-8'))

print(c.recv(1024).decode())

