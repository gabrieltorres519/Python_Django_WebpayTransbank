from datetime import datetime, timedelta

fechaCadena = '2024-01-18 23:12:40.163271'
ahora = datetime.strptime(fechaCadena, '%Y-%m-%d %H:%M:%S.%f') # Pasando la fecha de cadena de texto a ser objeto de la clase datetime.datetime

print(fechaCadena)
print(type(fechaCadena))
print(ahora)
print(type(ahora))

# La conversión a objeto es para poder luego ejecutar cálculos y aplicarle lógica
dentro_de_un_dia = ahora + timedelta(days=1)
print("Dentro de un día: " + str(dentro_de_un_dia))
