from PIL import Image, ImageFilter

#Contour
#Resulta em uma imagem preto e branco, destacando os contornos entre os objetos

img1 = Image.open('pintinho.jpg')

img2 = img1.filter(ImageFilter.CONTOUR)

img2.save('pintinhoContour.jpg')