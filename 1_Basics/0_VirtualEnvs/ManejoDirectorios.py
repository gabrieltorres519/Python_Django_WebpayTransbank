import os # Para obtener información de las carpetas/directorios
import shutil # Manipular archivos a nivel de linux, como renombrar, borrar, mover, etc

ruta = "/home/gabrielle/Documents/SICAP/Python_Django_Webpay_de_Transbank"
print(ruta)

ruta2 = os.path.dirname(os.path.abspath(__file__))
print(ruta2)

archivo_actual = os.path.abspath(__file__)
print(archivo_actual)

directorio_de_trabajo = os.getcwd()
print(directorio_de_trabajo)

if not os.path.isdir(ruta2 + '/miCarpetaNueva'): # Comprueba la no existencia de una carpeta 
    os.makedirs(ruta2 + '/miCarpetaNueva') # Creamos la carpeta

print(os.listdir(ruta2)) # Lista el contenido en una carpeta, dando su ruta
os.rename(ruta2 + '/miCarpetaNueva', ruta2 + '/miCarpeta_modificada')

os.rmdir(ruta2 + '/miCarpeta_modificada') # Para eliminar una carpeta (solo si está vacía)

if os.path.isdir(ruta2 + '/miCarpeta_modificada'): # Verificamos si la carpeta existe
    shutil.rmtree(ruta2 + '/miCarpeta_modificada') # Para borrar una carpeta (aunque tenga contenido)

shutil.copy(ruta2 + '/hola.html', ruta2 + "/holaychao.html") # copiar un archivo o carpeta y pegarlo con un nuevo nombre, manteniendo el original

shutil.move(ruta2 + '/hola.html', ruta2 + "/holaychao2.html") # Equivalente al cortar y pegar

# Una buena idea es primero mover el archivo y luego renombrarlo con un formato timestamp (hora y fecha)
