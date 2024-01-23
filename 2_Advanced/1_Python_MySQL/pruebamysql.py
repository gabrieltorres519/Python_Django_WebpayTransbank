# Importante destacar que éste archivo lo llamamos pruebamysql y no mysql 
# debido a que como es posible importar datos de archivos creados por 
# nosotros mismos, al momento de querer conectar a la base de datos habrá 
# confusión por parte de python de si usar la conexión a mysql o el archivo 
# que nosotros creamos, llamado mysql

from MySQL_Conexion import *


datos = getDatos('SELECT * FROM productos;')

for dato in datos:
    print(f"{dato[0]} - {dato[1]} - {numberFormat(dato[3])}")

