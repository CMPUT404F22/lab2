import socket
from multiprocessing import Process
from datetime import datetime
import os

MAX_PROCESSES = 4

def get_server_addr():
    return ("127.0.0.1", 8001)

def get_pid_log():
    return f'{datetime.now()}: [{os.getpid()}]'

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        request = "GET / HTTP/1.1\n\n"
        s.connect(get_server_addr())
        s.sendall(request.encode())
        data = s.recv(1024).decode()
    print(get_pid_log(), 'Client Received:', repr(data))

if __name__ == "__main__":
    for _ in range(MAX_PROCESSES):
        p  = Process(target=client)
        p.start()
