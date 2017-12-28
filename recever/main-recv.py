import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket

app = QApplication(sys.argv)

conn = QUdpSocket()
conn.bind(5020)


@conn.readyRead.connect
def func():
    while conn.hasPendingDatagrams():
        datagram, host, port = conn.readDatagram(conn.pendingDatagramSize())
    print(datagram)


sys.exit(app.exec_())
