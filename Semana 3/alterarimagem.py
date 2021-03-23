from PIL import Image

#abrir a imagem
img = Image.open('imagemNova.png')

#dimensões da imagem
#print(img.size)

#carregar a imagem para uma matriz
matriz = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        #print(matriz[i, j], end='')
        pass
    #print()

#alterando pixels da imagem
matriz[0, 0] = (20, 227, 69)
matriz[5, 2] = (120, 14, 227)

#salvar a imagem
img.save('imagemNovaAlterada.png')