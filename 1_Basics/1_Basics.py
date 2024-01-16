color = "verde"
numero = 13

if color == "verde":
    print("Es verde")
elif color == "azul":
    print("Es azul")
    if numero == 13:
        print("Se cumple 13")
    elif numero == 14:
        print("No se cumple 13")
else:
    print("Es otro color")

