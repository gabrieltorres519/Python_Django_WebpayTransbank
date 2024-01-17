# El siguiente código es para evitar hardcodear las periciones de
# input -> int(input('Inserte datos')), en lugar de eso se los 
# pasaremos directamente al ejecutar el programa 

import argparse

parser = argparse.ArgumentParser(description="Ejemplo de argparse")

parser.add_argument('-s', '--server', help="Servidor")

args = parser.parse_args()

if args.server:
    print(args.server)
else:
    print("No se recibió el nombre del server, por favor vuelva a intentarlo")

# python3 3_argparse.py --s hola