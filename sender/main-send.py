from socket import socket
from socket import SOCK_DGRAM as UDP

import numpy as np

from packetStructure import pStructure


ip_addr = ('127.0.0.1', 5020)

packet = np.zeros(1, dtype=pStructure)[0]

with socket(type=UDP) as conn:
    for name in iter(input, 'quit'):
        packet['name'] = name
        packet['data'][:] = np.random.randint(0, 9, 9)
        conn.sendto(packet.tostring(), ip_addr)
