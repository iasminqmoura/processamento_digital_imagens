from PIL import Image, ImageFilter

img = Image.open('tulipa.jpg')
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = matriz[i,j][0]
        g = 0 #g = matriz[i,j][1]
        b = 0 #b = matriz[i,j][2]
        matriz[i,j] = (r,g,b)

img.save('camada_r.jpg')

img = Image.open('tulipa.jpg')
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 0 #r = matriz[i,j][0]
        g = matriz[i,j][1]
        b = 0 #b = matriz[i,j][2]
        matriz[i,j] = (r,g,b)

img.save('camada_g.jpg')

img = Image.open('tulipa.jpg')
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 0 #r = matriz[i,j][0]
        g = 0 #g = matriz[i,j][1]
        b = matriz[i,j][2]
        matriz[i,j] = (r,g,b)

img.save('camada_b.jpg')