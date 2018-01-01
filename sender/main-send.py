from socket import socket
from socket import SOCK_DGRAM as UDP

import numpy as np

ip_addr = ('127.0.0.1', 5020)

pStructure = [
    ('name', 'a10'),
    ('data', float, (9,))
]


with socket(type=UDP) as conn:
    for name in iter(input, 'quit'):
        packet = np.zeros(1, dtype=pStructure)
        packet['name'] = name
        packet = packet.tostring()
        conn.sendto(packet, ip_addr)
