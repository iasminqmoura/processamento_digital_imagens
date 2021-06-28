import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    img1 = Image.open(arg01)

    img2 = img1.filter(ImageFilter.BLUR)

    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])