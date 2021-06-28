import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    img = Image.open(arg01)
    matriz = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = matriz[i, j][0]
            g = matriz[i, j][1]
            b = matriz[i, j][2]
            pixels = int((r + g + b) / 3)
            matriz[i, j] = (pixels, pixels, pixels)

    img.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])