import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket

import numpy as np

from plot import Canvas

pStructure = [
    ('name', 'a10'),
    ('data', float, (9,))
]


class sPlot(Canvas):
    def setup(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)


app = QApplication(sys.argv)

windows = {}

conn = QUdpSocket()
conn.bind(5020)


@conn.readyRead.connect
def func():
    while conn.hasPendingDatagrams():
        dataSize = conn.pendingDatagramSize()
        datagram, host, port = conn.readDatagram(dataSize)

    datagram = np.fromstring(datagram, dtype=pStructure)
    print(datagram)

    name = str(datagram['name'])
    print(name)
    if name not in windows:
        windows[name] = sPlot()
        windows[name].setWindowTitle(name)
        windows[name].show()


w = QWidget()
w.show()

sys.exit(app.exec_())
