from PIL import Image

def redimensionar():
    image = Image.open('logo.jpg')
    image.thumbnail((90, 90))
    image.save('logo3PIL.jpg')

redimensionar()