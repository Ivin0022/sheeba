from PyQt5.QtWidgets import QMainWindow, QDockWidget

import numpy as np

# our libraries
from lib.helpers import Application
from lib.packetStructure import pStructure
from lib.Network import UdpSocket
from plots import sPlot


windows = {}

with Application() as app:
    root = QMainWindow()

    conn = UdpSocket(root)

    @conn.setCallBack(5020)
    def func(datagram):
        datagram = np.fromstring(datagram[0], dtype=pStructure)[0]
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
