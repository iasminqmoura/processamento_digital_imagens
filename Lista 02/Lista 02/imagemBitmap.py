from PIL import Image

mode = "RGB"
size = (11, 12)
color = (255, 255, 255)

img = Image.new(mode, size, color)

matriz = img.load()

matriz[5, 0] = (0, 0, 0)

for i in range(4,7):
    for j in range(1,2):
        matriz[i, j] = (0, 0, 0)
#matriz[4, 1] = (0, 0, 0)
#matriz[5, 1] = (0, 0, 0)
#matriz[6, 1] = (0, 0, 0)

for i in range(3,8):
    for j in range(2,3):
        matriz[i, j] = (0, 0, 0)
#matriz[3, 2] = (0, 0, 0)
#matriz[4, 2] = (0, 0, 0)
#matriz[5, 2] = (0, 0, 0)
#matriz[6, 2] = (0, 0, 0)
#matriz[7, 2] = (0, 0, 0)

for i in range(2,9):
    for j in range(3,4):
        matriz[i, j] = (0, 0, 0)
#matriz[2, 3] = (0, 0, 0)
#matriz[3, 3] = (0, 0, 0)
#matriz[4, 3] = (0, 0, 0)
#matriz[5, 3] = (0, 0, 0)
#matriz[6, 3] = (0, 0, 0)
#matriz[7, 3] = (0, 0, 0)
#matriz[8, 3] = (0, 0, 0)

for i in range(2,9):
    for j in range(3,10):
        matriz[2, j] = (0, 0, 0)
        matriz[8, j] = (0, 0, 0)
#matriz[2, 4] = (0, 0, 0)
#matriz[8, 4] = (0, 0, 0)
#matriz[2, 5] = (0, 0, 0)
#matriz[8, 5] = (0, 0, 0)
#matriz[2, 6] = (0, 0, 0)
#matriz[8, 6] = (0, 0, 0)
#matriz[2, 7] = (0, 0, 0)
#matriz[8, 7] = (0, 0, 0)
#matriz[2, 8] = (0, 0, 0)
#matriz[8, 8] = (0, 0, 0)
#matriz[2, 9] = (0, 0, 0)
#matriz[8, 9] = (0, 0, 0)

for i in range(2,9):
    for j in range(10,11):
        matriz[i, j] = (0, 0, 0)
#matriz[2, 10] = (0, 0, 0)
#matriz[3, 10] = (0, 0, 0)
#matriz[4, 10] = (0, 0, 0)
#matriz[5, 10] = (0, 0, 0)
#matriz[6, 10] = (0, 0, 0)
#matriz[7, 10] = (0, 0, 0)
#matriz[8, 10] = (0, 0, 0)

img.save('imagemBitmap.png')
