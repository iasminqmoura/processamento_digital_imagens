from PIL import Image

img = Image.open('xicara.jpg')
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = matriz[i, j][0]
        g = matriz[i, j][1]
        b = matriz[i, j][2]
        p = (int((r + g + b)/3))
        matriz[i,j] = (p, p, p)

img.save('xicaraPB.jpg')