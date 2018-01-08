from PyQt5.QtNetwork import QUdpSocket, QHostAddress


# TODO: rewrite the decorator to make it more concise
# TODO: consider using NamedTuple as the data's data type  
class UdpSocket(QUdpSocket):
    """docstring for Socket"""

    def __init__(self, parent, *agrs, **kwargs):
        super(UdpSocket, self).__init__(parent, *agrs, **kwargs)

    def setCallBack(self, port):
        self.bind(port)

        def decorator(func):
            @self.readyRead.connect
            def wapper():
                while self.hasPendingDatagrams():
                    size = self.pendingDatagramSize()
                    data = self.readDatagram(size)
                func(data)
        return decorator
