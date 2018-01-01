import matplotlib; matplotlib.use('Qt5agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.setup()
        super(Canvas, self).__init__(fig)
        self.setParent(parent)

    def setup(self):
        pass
