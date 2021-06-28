from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Emboss
#Cria uma imagem destacando as diferentes regiões como se fossem relevos de diferentes alturas

img2 = img1.filter(ImageFilter.EMBOSS)

img2.save('pintinhoEmboss.jpg')