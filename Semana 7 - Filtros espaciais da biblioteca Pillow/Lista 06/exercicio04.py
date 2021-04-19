from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Edge Enhance
#Faz com que as bordas de diferentes regiões estejam mais visíveis, 
#distinguindo melhor regiões umas das outras

img2 = img1.filter(ImageFilter.EDGE_ENHANCE)

img2.save('pintinhoEdge.jpg')
