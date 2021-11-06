import sys

import matplotlib.pyplot as plt
import numpy as np

from main import *


class FirstApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.clickme)

    def clickme(self):
        f0 = self.horizontalSlider.value()
        v0 = self.doubleSpinBox_2.value()

        g = 9.8
        x0 = 0
        kat = np.pi * f0 / 180
        vy = v0 * np.sin(kat)
        vx = v0 * np.cos(kat)
        h = (vy * vy) / (2 * g) + 0.2 * ((vy * vy) / (2 * g))
        z = (2 * v0 * v0 * np.sin(kat) * np.cos(kat)) / g

        t_max = (2 * v0 * np.sin(kat)) / g
        t = np.arange(0.0, t_max, 0.001)

        yy = []
        xx = []

        for i in t:
            yy.append(x0 + vy * i - (g * i * i) / 2)
        for i in t:
            xx.append(x0 + vx * i)

        yy.append(x0 + vy * t_max - (g * t_max * t_max) / 2)
        xx.append(x0 + vx * t_max)

        if self.doubleSpinBox.value() == xx[len(xx) - 1]:
            self.label_5.setText("udało się!!")
        else:
            self.label_5.setText("Nie udało się!!")

        xt = self.doubleSpinBox.value()
        yt = 0

        if xt > z:
            z = xt + 0.1 * xt
        else:
            pass

        plt.plot(xx, yy, color='red')
        plt.plot(xt, yt, 'o-')
        plt.axis([0, z, 0, h])
        plt.show()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = FirstApp(MainWindow)
MainWindow.show()
app.exec_()
