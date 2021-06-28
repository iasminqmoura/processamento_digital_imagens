from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Smooth more
#Reduz ainda mais a nitidez nas bordas da imagem
img2 = img1.filter(ImageFilter.SMOOTH_MORE)

img2.save('pintinhoSmoothMore.jpg')