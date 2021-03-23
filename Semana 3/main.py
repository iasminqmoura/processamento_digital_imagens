from PIL import Image #importar a biblioteca Pillow

#criar uma imagem do zero 
mode = "RGB"
size = (10, 5) #(colunas, linhas)
color = (227, 127, 20)
img = Image.new(mode, size, color)
img.save('imagemNova.png')
#img.show() #não funciona no repl.it
