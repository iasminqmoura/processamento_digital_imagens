from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Sharpen
#Aumenta a nitidez da imagem
img2 = img1.filter(ImageFilter.SHARPEN)

img2.save('pintinhoSharpen.jpg')