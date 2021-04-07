# 01) O que significa o negativo de uma imagem?
#     Uma imagem negativa é obtida através da inversão de cores de uma imagem normal.

#Imagem colorida
from PIL import Image

imgColor = Image.open('colorido.jpg')
matrizColor = imgColor.load()

for i in range (imgColor.size[0]):
    for j in range (imgColor.size[1]):
        r = 255 - matrizColor[i, j][0]
        g = 255 - matrizColor[i, j][1]
        b = 255 - matrizColor[i, j][2]

        matrizColor[i, j] = (r, g, b)

imgColor.save('coloridoNegativo.jpg')

#Imagem escala de cinza
imgPB = Image.open('pretoBranco.jpg')
matrizPB = imgPB.load()

for i in range (imgPB.size[0]):
    for j in range (imgPB.size[1]):
        r = 255 - matrizPB[i, j][0]
        g = 255 - matrizPB[i, j][1]
        b = 255 - matrizPB[i, j][2]

        matrizPB[i, j] = (r, g, b)

imgPB.save('pretoBrancoNegativo.jpg')