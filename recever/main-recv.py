import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket

import numpy as np

from plot import Canvas
from packetStructure import pStructure


class sPlot(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)

    def setup(self):
        self.axes.plot(list(range(9)), [0] * 9)

    def updateFigure(self, data, col='r'):
        self.axes.cla()
        self.axes.plot(list(range(9)), data, col)
        self.draw()


app = QApplication(sys.argv)

windows = {}

conn = QUdpSocket()
conn.bind(5020)


@conn.readyRead.connect
def func():
    while conn.hasPendingDatagrams():
        dataSize = conn.pendingDatagramSize()
        datagram, host, port = conn.readDatagram(dataSize)

    datagram = np.fromstring(datagram, dtype=pStructure)[0]
    print(datagram)

    name = str(datagram['name'])
    print(name)
    if name not in windows:
        windows[name] = sPlot()
        windows[name].setWindowTitle(name)
        windows[name].show()
    windows[name].updateFigure(datagram['data'])


w = QWidget()
w.show()

sys.exit(app.exec_())
