from PIL import Image

mode = "RGB"
size = (4, 14)
color = (255, 255, 255)

img = Image.new(mode, size, color)

matriz = img.load()

for i in range(0,1):
    for j in range(0,14):
        matriz[i, j] = (255, 0, 25)

for i in range(1,2):
    for j in range(0,14):
        matriz[i, j] = (0, 255, 25)

for i in range(2,3):
    for j in range(0,14):
        matriz[i, j] = (90, 10, 90)

for i in range(3,4):
    for j in range(0,14):
        matriz[i, j] = (10, 30, 200)

img.save('imagemRGB.png')
