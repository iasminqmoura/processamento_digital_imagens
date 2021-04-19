from PIL import Image, ImageFilter

#Blur
#Aplica um efeito de embaçamento / enevoamento na imagem

img1 = Image.open('pintinho.jpg')

img2 = img1.filter(ImageFilter.BLUR)

img2.save('pintinhoBlur.jpg')