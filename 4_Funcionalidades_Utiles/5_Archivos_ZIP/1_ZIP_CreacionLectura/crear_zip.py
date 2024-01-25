import zipfile
import os

ruta = os.path.dirname(os.path.abspath(__file__))
archivo = zipfile.ZipFile(ruta+'/archivo.zip', 'w') # Crear el archivo con permisos de escritura

archivo.write('pdf_1706050646.029231.pdf', compress_type=zipfile.ZIP_DEFLATED) # El archivo que vamos a comprimir y el formato de compresión
archivo.close() # Al terminar de manipular el archivo lo cerramos
