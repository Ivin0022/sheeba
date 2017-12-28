from socket import socket
from socket import SOCK_DGRAM as UDP

ip_addr = ('127.0.0.1', 5020)


with socket(type=UDP) as conn:  # UDP
    conn.bind(ip_addr)
    while True:
        data, addr = conn.recvfrom(1024)  # buffer size is 1024 bytes
        print("received message:", data)
