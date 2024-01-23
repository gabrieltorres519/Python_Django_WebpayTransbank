import json
import os

ruta = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(ruta) # Dado que el archivo se encuentra un salto fuera del directorio de trabajo

with open(parent_directory+'/2_JSONejemplo.json') as file:
    datos = json.load(file)

# print(datos)
    
for dato in datos['post']:
    print(f"Título: {dato['titulo']}\nSlug: {dato['slug']}\nDetalle: {dato['detalle']}\nFecha: {dato['fecha']}")
    print("-------------------------------------")