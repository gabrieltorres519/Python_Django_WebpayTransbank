# Importante destacar que éste archivo lo llamamos pruebamysql y no mysql 
# debido a que como es posible importar datos de archivos creados por 
# nosotros mismos, al momento de querer conectar a la base de datos habrá 
# confusión por parte de python de si usar la conexión a mysql o el archivo 
# que nosotros creamos, llamado mysql

from MySQL_Conexion import *

# Ver datos

datos = getDatos('SELECT * FROM productos;')

# Dando formato y organizando para visualizar los datos recibidos
for dato in datos:
    print(f"{dato[0]} - {dato[1]} - {numberFormat(dato[3])}")


# Acrualizar datos 
    
setDatos("UPDATE productos SET precio=97987 WHERE id=1;")

# Crear nuevo producto

setDatos("INSERT INTO productos VALUES(null, 'Marco de foto','descripcion', 300)")

# Borrar un registro de la base

setDatos("DELETE FROM productos WHERE id=3")