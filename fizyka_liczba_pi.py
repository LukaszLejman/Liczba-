import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QSpinBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from math import *

import random
import time
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 50
        self.top = 50
        self.width = 1200
        self.height = 1000
        self.title = 'Obliczanie liczby π metodą Monte Carlo'
        self.initUI()
        self.showMaximized()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m = PlotCanvas(self, width=10, height=9)
        self.m.move(0,0)
        self.m.setFocus()
        self.r=100
        self.z=1
        self.osie(self.m.axes)
        self.button = QPushButton('Oblicz!', self)
        self.button.setGeometry(QtCore.QRect(1150, 50, 150, 50))
        self.button.clicked.connect(self.rysowanie)
        self.Logi = QtWidgets.QTextEdit(self)
        self.Logi.setGeometry(QtCore.QRect(1000, 100, 300, 800))
        self.Logi.setReadOnly(True)
        self.Logi.setObjectName("Logi")
        self.Logi.setFontPointSize(16)
        self.label_wynik = QtWidgets.QLabel(self)
        self.label_wynik.setWordWrap(True)
        self.label_wynik.setGeometry(QtCore.QRect(1000, 0, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_wynik.setFont(font)
        self.label_wynik.setText("Wpisz ilość punktów i naciśnij przycisk by obliczyć liczbę π metodą Monte Carlo.")
        self.inputspinbox = QSpinBox(self)
        self.inputspinbox.setGeometry(QtCore.QRect(1000, 50, 150, 50))
        self.inputspinbox.setRange(1,5000)
    def osie(self,axes):
        axes.clear()
        axes.set_title('Obliczanie liczby π metodą Monte Carlo')
        axes.set_ylim([-self.r,self.r])
        axes.set_xlim([-self.r,self.r])
        axes.axhline(y=0, color='k')
        axes.axvline(x=0, color='k')
        axes.set_xlabel('X')
        axes.set_ylabel('Y')
        self.m.draw()
    def rysowanie(self):
        self.z=self.inputspinbox.value()
        self.osie(self.m.axes)
        self.plot(self.m.axes)
    def plot(self, axes):
        circle = plt.Circle((0,0), self.r, color=str("b"),zorder=1)
        axes.add_patch(circle)
        w_kole=0
        self.m.draw()
        for a in range(0, self.z):
            pointx = random.uniform(-self.r, self.r)
            pointy = random.uniform(-self.r, self.r)
            if ((pow(pointx,2)+pow(pointy,2))<=pow(self.r,2)):
                axes.scatter(pointx,pointy,s=50,color=str("g"),zorder=2)
                w_kole=w_kole+1
            else:
                axes.scatter(pointx,pointy,s=50,color=str("r"),zorder=2)
        a=(4*w_kole)/self.z
        self.Logi.insertPlainText("Punkty w kole: "+str(w_kole)+".\n")
        self.Logi.insertPlainText("Liczba π obliczona dla "+str(self.z)+" punktow wynosi: "+str(a)+".\n")
        self.Logi.moveCursor(QtGui.QTextCursor.End)
        self.m.draw()

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        axes = self.figure.add_subplot(111)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
