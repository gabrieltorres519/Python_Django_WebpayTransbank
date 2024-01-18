while True:
    try: 
        numero = int(input("Ingrese un número (distinto de cero): "))
        resultado = 10/numero
        print(f"\nEl resultado de 10/{numero} es {resultado}")
        break
    except ZeroDivisionError:
        print("El valor insertado debe ser distinto de cero, intente nuevamente... ")
    except ValueError:
        print('Los datos ingresados no pueden ser texto, intente nuevamente...')