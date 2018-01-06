import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget
from PyQt5.QtNetwork import QUdpSocket

import numpy as np

# our libraries
from plots import sPlot
from packetStructure import pStructure

windows = {}

app = QApplication(sys.argv)

root = QMainWindow()

# TO DO: give the socket a parent, right now it's most likely
# being freed from memory by the GC at the end of execution
conn = QUdpSocket(root)
conn.bind(5020)


@conn.readyRead.connect
def func():
    # Don't know why while is used instead of if
    while conn.hasPendingDatagrams():
        datagram, host, port = conn.readDatagram(conn.pendingDatagramSize())
        # TODO: make it work w/o [0], probably wont find a way
        datagram = np.fromstring(datagram, dtype=pStructure)[0]
        print(datagram)

    # to convert from bytes to string
    name = datagram['name'].decode('utf-8')

    # TODO: consider using defaultdict
    # (defaultdict maybe more difficult for aunt to understand,
    #  also maybe unnecessarily complicated)
    if name not in windows:
        windows[name] = QDockWidget(name, root)
        windows[name].setWidget(sPlot())
        windows[name].setFloating(True)
        windows[name].show()
    windows[name].widget().updateFigure(datagram['data'])


root.setGeometry(100, 100, 600, 400)
root.show()

sys.exit(app.exec_())
