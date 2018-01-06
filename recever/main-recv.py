import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtNetwork import QUdpSocket

import numpy as np

from plots import sPlot
from packetStructure import pStructure

windows = {}
 
app = QApplication(sys.argv)

w = QMainWindow()

# TO DO: give the socket a parent, right now it's most likely
# being freed from memory by the GC at the end of execution
conn = QUdpSocket(w)
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

    # TODO: consider using defaultdict 
    # (defaultdict maybe more diffcult for aunty to understand)
    if name not in windows:
        tmpDock = QDockWidget(name, w)
        tmpDock.setWidget(sPlot())
        tmpDock.setFloating(True)
        tmpDock.show()
        windows[name] = tmpDock
    windows[name].widget().updateFigure(datagram['data'])

w.setGeometry(100, 100, 600, 400)
w.show()

sys.exit(app.exec_())
