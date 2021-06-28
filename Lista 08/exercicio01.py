import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget
from PyQt5.QtCore import QSize

def run():

    class MyWindow(QMainWindow):
        def __init__(self):
            super(MyWindow, self).__init__()
            self.setup_main_window()
            self.initUI()

        def setup_main_window(self):
            self.x = 600
            self.y = 480
            self.setMinimumSize(QSize(self.x, self.y))
            self.wid = QWidget(self)
            self.setCentralWidget(self.wid)
            self.layout = QGridLayout()
            self.wid.setLayout(self.layout)

        def initUI(self):
            self.texto = QLabel("Aplicação do filtro de contorno", self)
            self.texto.adjustSize()
            self.texto.setAlignment(QtCore.Qt.AlignCenter)

            self.b1 = QtWidgets.QPushButton(self)
            self.b1.setText("Open me")
            self.b1.clicked.connect(self.open_file)

            self.b2 = QtWidgets.QPushButton(self)
            self.b2.setText("Transforme me?")
            self.b2.clicked.connect(self.transform_me)

            self.imagem1 = QLabel(self)
            self.endereco1 = 'colored1.jpg'
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)
            self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

            self.imagem2 = QLabel(self)
            self.endereco2 = './colored1.jpg'
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)
            self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

            self.layout.addWidget(self.texto, 0, 0, 1, 2)
            self.layout.addWidget(self.b1, 2, 0)
            self.layout.addWidget(self.imagem1, 1, 0)
            self.layout.addWidget(self.imagem2, 1, 1)
            self.layout.addWidget(self.b2, 2, 1)
            self.layout.setRowStretch(0, 0)
            self.layout.setRowStretch(1, 1)
            self.layout.setRowStretch(2, 0)

        def open_file(self):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                caption='Open image',
                                                                directory=QtCore.QDir.currentPath(),
                                                                filter='All files (*.*);; Images (*.jpg;*.png)',
                                                                initialFilter='All files (*.*)')
            print(fileName)
            if fileName != ' ':
                self.endereco1 = fileName
                self.pixmap1 = QtGui.QPixmap(self.endereco1)
                self.pixmap1 = self.pixmap1.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
                self.imagem1.setPixmap(self.pixmap1)

        def transform_me(self):
            self.entrada = self.endereco1
            self.saida = 'converted.jpg'
            self.script = './countourImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)


    def window():
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())

    window()

if __name__== "__main__":
    run()