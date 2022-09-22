import socket
from multiprocessing import Process

MAX_PROCESSES = 5

def init_server_socket():
    HOST = ''
    PORT = 8001
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse same bind port
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    return server_socket

def process_clients(server_socket):
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                print("Received:", data.decode())
                conn.sendall(data)


if __name__ == "__main__":
    s = init_server_socket()
    child_processes = [Process(target=process_clients, args=(s,)) for _ in range(MAX_PROCESSES)]
    for p in child_processes:
        p.start()
