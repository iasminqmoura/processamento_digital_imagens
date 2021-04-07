#Filtro negativo
from PIL import Image

#Abrir imagem
img = Image.open('imagemPB.jpg')
#print(img.size)

#Carregar a imagem para uma matriz
matriz = img.load()

#Realizar as operações pixel a pixel de transformações
gamma = 0.5
for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma * 255)
        g = int((matriz[i, j][1]/255) ** gamma * 255)
        b = int((matriz[i, j][2]/255) ** gamma * 255)

        matriz[i, j] = (r, g, b)

#Salvar a imagem
img.save('ImagemPBGamma0pt5.jpg')