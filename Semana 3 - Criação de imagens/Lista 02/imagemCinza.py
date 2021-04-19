from PIL import Image

mode = "RGB"
size = (4, 8)
color = (255, 255, 255)

img = Image.new(mode, size, color)

matriz = img.load()

for i in range(0,4):
    for j in range(0,1):
        matriz[i, j] = (0, 0, 0)

for i in range(0,1):
    for j in range(0,8):
        matriz[i, j] = (0, 0, 0)
        
for i in range(0,4):
    for j in range(7,8):
        matriz[i, j] = (0, 0, 0)

for i in range(1,2):
    for j in range(1,7):
        matriz[i, j] = (200, 200, 200)

for i in range(2,3):
    for j in range(1,7):
        matriz[i, j] = (120, 120, 120)

for i in range(3,4):
    for j in range(1,7):
        matriz[i, j] = (88, 88, 88)

img.save('imagemCinza.png')
