from barcode import generate
import os

ruta = os.path.dirname(os.path.abspath(__file__))
numero = '123456789012'
generate('Code128', numero, output=os.path.join(ruta, 'barra'))
