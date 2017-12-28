from socket import socket
from socket import SOCK_DGRAM as UDP


ip_addr = ('127.0.0.1', 5020)

with socket(type=UDP) as conn:
    for msg in iter(input, 'quit'):
        conn.sendto(msg.encode('utf-8'), ip_addr)
