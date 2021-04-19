# 02) O que significa a correção gama de uma imagem?
#     Gamma é o valor relativo de claro e escuro da imagem.
#     O que se percebe como resultado para valores de gama menores do que 1? E para valores maiores do que 1?
#     Em valores menores que 1 nota-se que as imagens são mais claras. Maiores que 1 as imagens ficam mais escuras.

#Imagem colorida
from PIL import Image

gamma = [0.25, 0.5, 1, 2, 3]

img = Image.open('pretoBranco.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[0] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[0] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[0] * 255)

        matriz[i, j] = (r, g, b)

img.save('pretoBranco0pt25.jpg')

img = Image.open('pretoBranco.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[1] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[1] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[1] * 255)

        matriz[i, j] = (r, g, b)

img.save('pretoBranco0pt5.jpg')

img = Image.open('pretoBranco.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[2] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[2] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[2] * 255)

        matriz[i, j] = (r, g, b)

img.save('pretoBranco1pt0.jpg')

img = Image.open('pretoBranco.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[3] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[3] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[3] * 255)

        matriz[i, j] = (r, g, b)

img.save('pretoBranco2pt0.jpg')

img = Image.open('pretoBranco.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[4] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[4] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[4] * 255)

        matriz[i, j] = (r, g, b)

img.save('pretoBranco3pt0.jpg')


img = Image.open('colorido.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[0] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[0] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[0] * 255)

        matriz[i, j] = (r, g, b)

img.save('colorido0pt25.jpg')

img = Image.open('colorido.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[1] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[1] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[1] * 255)

        matriz[i, j] = (r, g, b)

img.save('colorido0pt5.jpg')

img = Image.open('colorido.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[2] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[2] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[2] * 255)

        matriz[i, j] = (r, g, b)

img.save('colorido1pt0.jpg')

img = Image.open('colorido.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[3] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[3] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[3] * 255)

        matriz[i, j] = (r, g, b)

img.save('colorido2pt0.jpg')

img = Image.open('colorido.jpg')
matriz = img.load()

for i in range (img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i, j][0]/255) ** gamma[4] * 255)
        g = int((matriz[i, j][1]/255) ** gamma[4] * 255)
        b = int((matriz[i, j][2]/255) ** gamma[4] * 255)

        matriz[i, j] = (r, g, b)

img.save('colorido3pt0.jpg')
