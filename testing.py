import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt6 import QtWidgets
import numpy as np
import sys
from sympy.parsing.latex import parse_latex
app=QtWidgets.QApplication(sys.argv)
window=QtWidgets.QMainWindow()
window.resize(800,600)

plot_widget=pg.PlotWidget()
window.setCentralWidget(plot_widget)

x=np.linspace(-10,10,100)
#Variable array called X

expression=parse_latex("x^2")
#When parsing, it does not use the x array, uses a different sympy variable, so another
#Data set is not created for PyQt to graph, fix this IMMEDIATELY
functions=[expression]


for item in functions:
    plot_widget.plot(x,item)
plot_widget.setXRange(-10,10)
plot_widget.setYRange(-1,10)
plot_widget.showGrid(x=True,y=True)
window.show()
sys.exit(app.exec())