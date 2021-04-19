from PIL import  Image, ImageFilter

img1 = Image.open('natureza.jpg')

#Sharpen
kernelS = ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 5, -1, 0, -1, 0), 1, 0)
img2 = img1.filter(kernelS)

#Blur
kernelB  = ImageFilter.Kernel((3, 3), ((1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9)), 1, 0)
img3 = img2.filter(kernelB)

img2.save('naturezaSharpen.jpg')
img3.save('naturezaSharpenMediana.jpg')
