# Ámbito o variables globales

nombre = "Gabriel"


def miFuncion():
    nombre = "César" # Ámbito o variable local
    return nombre

def convertir(texto):
    return texto.upper()

def otraFuncion(num1, num2):
    return f"La suma de {num1} + {num2} es {num1 + num2}"

year = lambda numero: f"El año es {numero}"

print(miFuncion())
print(convertir("hola"))
print(otraFuncion(4,5))
print(year(2024))
