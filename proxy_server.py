import socket
import os
from multiprocessing import Process
from datetime import datetime

MAX_PROCESSES = 4

def request_to_google(request):
    HOST = "www.google.com"
    PORT = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request)
        data = s.recv(1024)
    return data

def init_server_socket():
    HOST = ''
    PORT = 8001
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse same bind port
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    return server_socket

def get_pid_log():
    return f'{datetime.now()}: [{os.getpid()}]'

def process_clients(server_socket):
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(get_pid_log(), "Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                response = request_to_google(data)
                conn.sendall(response)
            print(get_pid_log(), "Processed", addr)


if __name__ == "__main__":
    s = init_server_socket()
    child_processes = [Process(target=process_clients, args=(s,)) for _ in range(MAX_PROCESSES)]
    for p in child_processes:
        p.start()
    
