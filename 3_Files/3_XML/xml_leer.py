from xml.dom import minidom # En informática DOM se refiere comunmente a apuntar al cuerpo de algún contenedor de datos
import os

ruta = os.path.dirname(os.path.abspath(__file__))

xml = minidom.parse(ruta+"/ejemplo.xml") # Parse es revisar la sintaxis y lógica del código

docs = xml.getElementsByTagName("doc")  # Posicionarnos dentro del tag name, sabiendo que tenemos uno base llamado root y quetemos la info contenida en el tag llamado doc 
# En el caso de que el archivo xml que se intenta leer no tenga el tag 'doc', retornará un arreglo (lista) vacío

print(docs)

for doc in docs:
    nodo1 = doc.getElementsByTagName("nodo1")[0]
    print(f"nodo 1 = {nodo1.firstChild.data}")
