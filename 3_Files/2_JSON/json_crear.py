import json
import os

ruta2 = os.path.dirname(os.path.abspath(__file__))

data = {} # Diccionario

data['post'] = [] # Nodo para el diccionario

for i in range(1, 11):
    data['post'].append({ # Datos que contendrá el nodo (como se puede ver, puede ser una entidad completa)
        'id': i,
        'titulo': f"Titulo de la publicación {i}",
        'slug': f"titulo-de-la-publicacion-{i}",
        'detalle': f"texto de detalle {i}",
        'fecha': '2024-01-23' 
    })

print(type(data))

with open(ruta2+'ejemplo.json', 'w') as file:
    json.dump(data,file, indent=4) # Insertando los datos en el archivo que se creará