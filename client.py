import socket

HOST = "www.google.com"
PORT = 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    request = "GET / HTTP/1.1\n\n"
    s.connect((HOST, PORT))
    s.sendall(request.encode())
    data = s.recv(1024).decode()
print('Received', repr(data))