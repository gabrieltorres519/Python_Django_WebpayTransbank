import qrcode 
from PIL import Image
import os

ruta = os.path.dirname(os.path.abspath(__file__))

face = Image.open(ruta+"/logo.jpg")

qr_big = qrcode.QRCode(error_correction= qrcode.constants.ERROR_CORRECT_H)

qr_big.add_data("https://www.instagram.com/gabrielletorricelli/")
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

# Toma el logo y logra que quede centrado en el QR con los cálculos siguientes
pos = ((img_qr_big.size[0] - face.size[0]) // 2,(img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save(ruta+"/qr2.png")