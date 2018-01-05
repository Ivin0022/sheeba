import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket

import numpy as np

from plots import sPlot
from packetStructure import pStructure


app = QApplication(sys.argv)

windows = {}

# TO DO: give the socket a parent, right now it's most likely
# being freed from memory by the GC at the end of execution
conn = QUdpSocket()
conn.bind(5020)


@conn.readyRead.connect
def func():
    while conn.hasPendingDatagrams():
        dataSize = conn.pendingDatagramSize()
        datagram, host, port = conn.readDatagram(dataSize)

    datagram = np.fromstring(datagram, dtype=pStructure)[0]
    print(datagram)

    # to convert from bytes to string
    name = datagram['name'].decode('utf-8')
    print(name)
    if name not in windows:
        windows[name] = sPlot()
        windows[name].setWindowTitle(name)
        windows[name].show()
    windows[name].updateFigure(datagram['data'])


w = QWidget()
w.show()

sys.exit(app.exec_())
