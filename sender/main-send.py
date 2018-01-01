from socket import socket
from socket import SOCK_DGRAM as UDP

import numpy as np
from random import randint

from packetStructure import pStructure


ip_addr = ('127.0.0.1', 5020)


with socket(type=UDP) as conn:
    for name in iter(input, 'quit'):
        packet = np.zeros(1, dtype=pStructure)
        packet['name'] = name
        packet['data'][0][:] = [randint(0, 10) for i in range(9)]
        packet = packet.tostring()
        conn.sendto(packet, ip_addr)
