from PIL import ImageFilter, Image

img1 = Image.open('flor.jpg')

kernel = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1, 0)

img2 = img1.filter(kernel)

img2.save('florFiltro02.jpg')
