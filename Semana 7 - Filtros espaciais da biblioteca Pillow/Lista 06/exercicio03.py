from PIL import Image, ImageFilter

#Detail
#Melhora os detalhes e cores da imagem, dando uma maior nitidez a diferentes áreas

img1 = Image.open('pintinho.jpg')

img2 = img1.filter(ImageFilter.DETAIL)

img2.save('pintinhoDetail.jpg')