from PIL import Image

img = Image.open('logo.jpg')

img = img.rotate(180)
img.show()