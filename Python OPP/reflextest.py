from PySide6 import QtWidgets, QtCore, QtGui
import sys
import random
import time


class ReflexTest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.start = QtWidgets.QPushButton("Start")
        self.start.clicked.connect(self.game) 

        self.introlayout = QtWidgets.QGridLayout()
        self.introlayout.addWidget(self.start)
        self.setLayout(self.introlayout) 

    def game(self):
            self.layout = QtWidgets.QVBoxLayout()
            self.text = QtWidgets.QLabel("Wait for green!",
                                        alignment=QtCore.Qt.AlignCenter)
            self.text.setStyleSheet("font-weight:1000;")

            self.num = random.random()
            print(self.num)

            self.layout = QtWidgets.QVBoxLayout()
            self.layout.addWidget(self.text)
            self.setLayout(self.layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    widget = ReflexTest()
    widget.resize(800,400)
    widget.show()
    sys.exit(app.exec())
