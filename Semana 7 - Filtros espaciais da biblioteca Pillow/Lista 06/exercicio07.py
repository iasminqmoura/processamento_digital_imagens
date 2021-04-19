from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Find Edges
#Explicita as bordas das regiões presentes na imagem

img2 = img1.filter(ImageFilter.FIND_EDGES)

img2.save('pintinhoFindEdge.jpg')
