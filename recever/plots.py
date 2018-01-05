from AbstractPlotCanvas import Canvas


class sPlot(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)

    def setup(self):
        self.axes.plot(list(range(9)), [0] * 9)

    def updateFigure(self, data, col='r'):
        self.axes.cla()
        self.axes.plot(list(range(9)), data, col)
        self.draw()
