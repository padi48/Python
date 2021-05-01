from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from main import StockInfo

def window():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(650,250,500,500)
    win.setWindowTitle("Trading bot!")

    label = QtWidgets.QLabel(win)
    label.move(200,0)
    label.setText("Python trading bot!")

    search_bar = QtWidgets.Q

    win.show()
    sys.exit(app.exec_())

window()
