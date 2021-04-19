from PIL import Image, ImageFilter

#Abrir a imagem
img1 = Image.open('carros.jpg')

#Criar o kernel
kernel = ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)

#Aplicar o kernel na imagem
img2 = img1.filter(kernel)

#Salvar a imagem resultante
img2.save('carrosBordas.jpg')