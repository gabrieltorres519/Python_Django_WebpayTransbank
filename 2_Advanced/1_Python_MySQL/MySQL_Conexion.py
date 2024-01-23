import mysql.connector
from mysql.connector import errorcode

def conectar():
    try: 
        return mysql.connector.connect(
            host='localhost',
            port= 3306,
            user= 'gabriel',
            passwd= '***',
            database= 'PythonMySQL'
        )
    except mysql.connector.Error as e: # El código estarpa atento al tipo de excepción de mysql 
        print(f"error de conexión {e}")
        exit()

def getDatos(sql): # SQL es la consulta
    cn = conectar() # Ejecución del método de conexión
    cur = cn.cursor(buffered=True) # Con los cursores accesamos a los datos 
    try:
        cur.execute(sql) # Ejecutamos el cursor y le pasamos la consulta sql
        return cur.fetchall() # Para que retorne todos los datos obtenidos de la consulta 
    except mysql.connector.Error as e:
        print(f"error con la consulta: {e}")
        exit()
    cn.close()


def getDato(sql): # SQL es la consulta
    cn = conectar() # Ejecución del método de conexión
    cur = cn.cursor(buffered=True) # Con los cursores accesamos a los datos 
    try:
        cur.execute(sql) # Ejecutamos el cursor y le pasamos la consulta sql
        return cur.fetchone() # Para que retorne el dato obrenido de la consulta 
    except mysql.connector.Error as e:
        print(f"error con la consulta: {e}")
        exit()
    cn.close()

def setDatos(sql): # SQL es la consulta
    cn = conectar() # Ejecución del método de conexión
    cur = cn.cursor(buffered=True) # Con los cursores accesamos a los datos 
    try:
        cur.execute(sql) # Ejecutamos el cursor y le pasamos la consulta sql
        cn.commit() # Para enviar los nuevos datos a ingresar a la base 
    except mysql.connector.Error as e:
        print(f"error con la consulta: {e}")
        exit()
    cn.close()

def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return "{:,}".format(numero).replace(",",".")