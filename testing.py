import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt6 import QtWidgets
import numpy as np
import sys
app=QtWidgets.QApplication(sys.argv)
window=QtWidgets.QMainWindow()
window.resize(800,600)

plot_widget=pg.PlotWidget()
window.setCentralWidget(plot_widget)

x=np.linspace(-10,10,100)
y=x**2

plot_widget.showGrid(x=True,y=True)

plot_widget.plot(x,y)
window.show()
sys.exit(app.exec())
