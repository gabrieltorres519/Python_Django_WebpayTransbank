import xml.etree.cElementTree as ET 
import os

ruta = os.path.dirname(os.path.abspath(__file__))

root = ET.Element("root") # Creando el primer tag (como si fuera la etiqueta <html></html> en un archivo)

# Crear la estructura con un ciclo for

# <root>
#     <doc>
#         <nodo1 name="nodo"> Texto nodo 1 0</nodo1>
#         <nodo2 atributo="manzana"> Texto nodo 2 0</nodo1>
#     </doc>
#     <doc>
#
#     </doc>
# </root>

for numero in range(1, 4):
    doc = ET.SubElement(root, "doc") # Creación del nodo doc dentro de root
    ET.SubElement(doc, "nodo1", name="manzana").text=f"Texto nodo1 {i}"

archivo = ET.ElementTree(root)
archivo.write(ruta+'/ejemplo.xml')