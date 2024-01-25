import cv2
import os

ruta = os.path.dirname(os.path.abspath(__file__))
src = cv2.imread(ruta+'/logo.jpg', cv2.IMREAD_UNCHANGED)
porcentage = 50

ancho = int(src.shape[1] * porcentage/100)
alto = int(src.shape[0] * porcentage/100)
 
dsize = (ancho, alto)

salida = cv2.resize(src, dsize)

cv2.imwrite(os.path.join(ruta, 'logo2.jpg'), salida)
