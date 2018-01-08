import sys
from PyQt5.QtWidgets import QApplication

from contextlib import contextmanager


@contextmanager
def Application():
    """Create a QApplication instance and Exec() it"""
    app = QApplication(sys.argv)
    yield app
    sys.exit(app.exec_())
