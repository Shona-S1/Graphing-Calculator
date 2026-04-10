import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt6 import QtWidgets,QtCore,QtGui, uic
import pyqtgraph.opengl as gl
import numpy as np
import sys
from sympy.parsing.latex import parse_latex
from sympy import symbols,lambdify
app=QtWidgets.QApplication(sys.argv)
window=QtWidgets.QMainWindow()
window.resize(800,600)

sidebar=uic.loadUi(r"C:\Users\Mark\Documents\The Project\test.ui",window)

plot_widget=pg.PlotWidget()
sidebar= QtWidgets.QWidget()
window.setCentralWidget(plot_widget)
array=np.linspace(-10,10,100)
#Array that acts as the x values for the plot

x=symbols('x')
expression=parse_latex('x^2')
f=lambdify(x,expression,'math')
#Create a lambda function from the sympy expression to evaluate it for the array of x values

functions=[expression]

for item in functions:
    plot_widget.plot(array,f(array))
    #Plot the array as x, and evaluate the function for each value in the array
plot_widget.setXRange(-10,10)
plot_widget.setYRange(-10,10)
plot_widget.showGrid(x=True,y=True)

window.show()
sys.exit(app.exec())