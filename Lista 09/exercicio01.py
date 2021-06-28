import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize

def run():

    class MyWindow(QMainWindow):
        def __init__(self):
            super(MyWindow, self).__init__()
            self.setup_main_window()
            self.initUI()

        def setup_main_window(self):
            self.x = 700
            self.y = 480
            self.setMinimumSize(QSize(self.x, self.y))
            self.setWindowTitle("Aprimoramento do Aplicativo")
            self.wid = QWidget(self)
            self.setCentralWidget(self.wid)
            self.layout = QGridLayout()
            self.wid.setLayout(self.layout)

        def initUI(self):
            self.barraDeMenu = self.menuBar()

            self.menuArquivo = self.barraDeMenu.addMenu("&Arquivo")
            self.menuTransformacoes = self.barraDeMenu.addMenu("&Transformações")

            self.opcaoSobre = self.barraDeMenu.addAction("&Sobre")
            self.opcaoSobre.triggered.connect(self.exibir_mensagem)

            self.opcaoAbrir = self.menuArquivo.addAction("&Abrir arquivo")
            self.opcaoAbrir.triggered.connect(self.open_file)

            self.opcaoFechar = self.menuArquivo.addAction("&Fechar programa")
            self.opcaoFechar.triggered.connect(self.close)

            self.opcaoBlur = self.menuTransformacoes.addAction("&Blur")
            self.opcaoBlur.triggered.connect(self.transform_blur)

            self.opcaoContour = self.menuTransformacoes.addAction("&Contour")
            self.opcaoContour.triggered.connect(self.transform_contour)

            self.opcaoDetail = self.menuTransformacoes.addAction("&Detail")
            self.opcaoDetail.triggered.connect(self.transform_detail)

            self.opcaoEmboss = self.menuTransformacoes.addAction("&Emboss")
            self.opcaoEmboss.triggered.connect(self.transform_emboss)

            self.opcaoFindEdge = self.menuTransformacoes.addAction("&Find Edges")
            self.opcaoFindEdge.triggered.connect(self.transform_edges)

            self.opcaoGrayscale = self.menuTransformacoes.addAction("&Grayscale")
            self.opcaoGrayscale.triggered.connect(self.trasnform_grayscale)

            self.texto = QLabel("Atualizando o aplicativo", self)
            self.texto.adjustSize()
            self.texto.setAlignment(QtCore.Qt.AlignCenter)

            self.imagem1 = QLabel(self)
            self.endereco1 = 'images/colored1.jpg'
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)
            self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

            self.imagem2 = QLabel(self)
            self.endereco2 = 'images/colored1.jpg'
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)
            self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

            self.layout.addWidget(self.texto, 0, 0, 1, 2)
            self.layout.addWidget(self.imagem1, 1, 0)
            self.layout.addWidget(self.imagem2, 1, 1)
            self.layout.setRowStretch(0, 0)
            self.layout.setRowStretch(1, 1)

        def open_file(self):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                caption='Open image',
                                                                directory=QtCore.QDir.currentPath(),
                                                                filter='All files (*.*);; Images (*.jpg;*.png)',
                                                                initialFilter='Images (*.jpg;*.png)')
            print(fileName)
            if fileName != ' ':
                self.endereco1 = fileName
                self.pixmap1 = QtGui.QPixmap(self.endereco1)
                self.pixmap1 = self.pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                self.imagem1.setPixmap(self.pixmap1)

        def transform_blur(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_blur.jpg'
            print(self.entrada[:-4])
            self.script = './blurImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_contour(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_contour.jpg'
            print(self.entrada[:-4])
            self.script = './contourImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_detail(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_detail.jpg'
            print(self.entrada[:-4])
            self.script = './detailImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_emboss(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_emboss.jpg'
            print(self.entrada[:-4])
            self.script = './embossImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_edges(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_edges.jpg'
            print(self.entrada[:-4])
            self.script = './findEdgesImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def trasnform_grayscale(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_grayscale.jpg'
            print(self.entrada[:-4])
            self.script = './grayscaleImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def end_transform(self):
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        def exibir_mensagem(self):
            self.mensagem = QMessageBox()
            self.mensagem.setIcon(QMessageBox.Information)
            self.mensagem.setWindowTitle("Sobre o aplicativo")
            self.mensagem.setText("Atualização desenvolvida por:\nIasmin Quirino Moura")
            self.mensagem.setInformativeText("Aplicativo atualizado para aplicação de transformações "
                                          "em imagens. \nTransformações utilizadas: Blur, Contour, Detail, "
                                             "Emboss, Find Edges, Grayscale.\n\n"
                                          "Ituiutaba - MG"
                                          "\n28/06/2021")
            self.mensagem.exec_()

    def window():
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())

    window()

if __name__== "__main__":
    run()