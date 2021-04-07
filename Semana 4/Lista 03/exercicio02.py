# 02) O que significa a correção gama de uma imagem?
#     Gamma é o valor relativo de claro e escuro da imagem.
#     O que se percebe como resultado para valores de gama menores do que 1? E para valores maiores do que 1?

#Imagem colorida
from PIL import Image

imgColor = Image.open('colorido.jpg')
matrizColor = imgColor.load()

gamma = 0.5

for i in range (imgColor.size[0]):
    for j in range (imgColor.size[1]):
        r = int((matrizColor[i, j][0]/255) ** gamma * 255)
        g = int((matrizColor[i, j][1]/255) ** gamma * 255)
        b = int((matrizColor[i, j][2]/255) ** gamma * 255)

        matrizColor[i, j] = (r, g, b)

if gamma == 0.25:
    imgColor.save('coloridoGamma0pt25.jpg')
elif gamma == 0.5:
    imgColor.save('coloridoGamma0pt5.jpg')
elif gamma == 1:
    imgColor.save('coloridoGamma1pt0.jpg')
elif gamma == 2:
    imgColor.save('coloridoGamma2pt0.jpg')
elif gamma == 3:
    imgColor.save('coloridoGamma3pt0.jpg')

#Imagem escala de cinza
imgPB = Image.open('pretoBranco.jpg')
matrizPB = imgPB.load()

gammaPB = 0.5

for i in range (imgPB.size[0]):
    for j in range (imgPB.size[1]):
        r = int((matrizPB[i, j][0]/255) ** gammaPB * 255)
        g = int((matrizPB[i, j][1]/255) ** gammaPB * 255)
        b = int((matrizPB[i, j][2]/255) ** gammaPB * 255)

        matrizPB[i, j] = (r, g, b)

if gammaPB == 0.25:
    imgColor.save('pretoBrancoGamma0pt25.jpg')
elif gammaPB == 0.5:
    imgColor.save('pretoBrancoGamma0pt5.jpg')
elif gammaPB == 1:
    imgColor.save('pretoBrancoGamma1pt0.jpg')
elif gammaPB == 2:
    imgColor.save('pretoBrancoGamma2pt0.jpg')
elif gammaPB == 3:
    imgColor.save('pretoBrancoGamma3pt0.jpg')