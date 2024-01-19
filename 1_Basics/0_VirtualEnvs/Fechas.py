from datetime import datetime, date, time, timedelta

ahora = datetime.now()
hoy = datetime.today()
current_time = datetime.now().strftime("%H:%M:%S")
fecha = date.today()
formato_day = "%d-%m-%Y"

print(ahora)
print(hoy)
print(current_time)
print(fecha)


print(f"año: {ahora.day}-{ahora.month}-{ahora.year}")

# En la mayoría de bases de datos las fechas se almacenan con formato
# Año-Mes-Día
print(hoy.strftime(formato_day))

# Conversión de fechas a formato timestamp
print(f"fecha= {hoy} | timestamp= {datetime.timestamp(hoy)}") # Se usa mucho cuando tienes que hacer APIs con JWT, pues a los tokens
                                                              # hay que pasarles un parámetro de fecha y en general se le pasa en un 
                                                              # formato timesstamp, esa fecha es para poder darle una vigencia a esos 
                                                              # tokens 

# Cómo restarle días a una fecha 
print(f"fecha {fecha} menos un día es: {fecha-timedelta(days=10)}")

# Saber cúal es el día de la semana con el que se va a trabajar
print(f"día de la semana {datetime.weekday(fecha)}")