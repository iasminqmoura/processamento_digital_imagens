import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.cont = 1

        self.x = 450
        self.y = 240
        self.setMinimumSize(QSize(self.x, self.y))

        self.image01 = QLabel(self)
        self.end01 = QtGui.QPixmap('original_colored.jpg')
        self.image01.setPixmap(self.end01)
        self.image01.setGeometry((self.x / 2) - 150, 20, 300, 168)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Trocar imagem")
        self.b1.setGeometry(20,self.image01.frameGeometry().height() + 30, self.x - 40, 20)
        self.b1.clicked.connect(self.button_clicked)

    def button_clicked(self):
        if(self.cont == 1):
            self.end01 = QtGui.QPixmap('original_grayscale.jpg')
            self.image01.setPixmap(self.end01)
            self.cont = 0
        else:
            self.end01 = QtGui.QPixmap('original_colored.jpg')
            self.image01.setPixmap(self.end01)
            self.cont = self.cont + 1

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
