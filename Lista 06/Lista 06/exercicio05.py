from PIL import Image, ImageFilter

img1 = Image.open('pintinho.jpg')

#Edge Enhance More
#Faz com que as bordas de diferentes regiões estejam mais visíveis, 
#distinguindo melhor regiões umas das outras.
#É mais intenso que o Edge Enhance

img2 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)

# Salvar a imagem resultante
img2.save('pintinhoEdgeMore.jpg')