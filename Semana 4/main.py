#Filtro negativo
from PIL import Image

#Abrir imagem
img = Image.open('imagemPB.jpg')
#print(img.size)

#Carregar a imagem para uma matriz
matriz = img.load()

#Realizar as operações pixel a pixel de transformações
for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = 255 - matriz[i, j][0]
        g = 255 - matriz[i, j][1]
        b = 255 - matriz[i, j][2]

        matriz[i, j] = (r, g, b)

#Salvar a imagem
img.save('novaImagemPB.jpg')