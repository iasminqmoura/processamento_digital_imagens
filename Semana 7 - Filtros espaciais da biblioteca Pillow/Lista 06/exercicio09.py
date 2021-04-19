from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Smooth
#Reduz a nitidez nas bordas da imagem
img2 = img1.filter(ImageFilter.SMOOTH)

img2.save('pintinhoSmooth.jpg')