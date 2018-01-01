import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket

app = QApplication(sys.argv)

conn = QUdpSocket()
conn.bind(5020)

windows = {}


@conn.readyRead.connect
def func():
    while conn.hasPendingDatagrams():
        dataSize = conn.pendingDatagramSize()
        datagram, host, port = conn.readDatagram(dataSize)
    print(datagram)

    if datagram not in windows:
        windows[datagram] = QWidget()
        windows[datagram].setWindowTitle(str(datagram))
        windows[datagram].show()


w = QWidget()
w.show()

sys.exit(app.exec_())
