# Cuando hay errores en python la consola imprime un objeto error que entre otras cosas
# nos dice el tipo de excepción o problema que ha ocurrido y aproximadamente dónde ha
# ocurrido.

try:
    print(5/0)
except:
    print("Ocurrio un error!")
finally:
    print("Terminó la ejecución")

# Usando try: podremos evitar la impresión se éste error complejo por consola, y mejor 
# mostraremos algo más sencillo al usuario
    

# El siguiente es el mismo ejemplo pero con opciones más complejas
        
try:
    print(5/0)
#except Exception as e: # Se usa el objeto con el tipo de error
#    print(e.__class__) # Imprimimos en pantalla el tipo de error
except ZeroDivisionError:
    print("No es posible dividir por cero") # Ya que hemos identificado la excepción, 
                                            # podemos decidir qué hacer al encontrarla

