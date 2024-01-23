import xlrd
import os

ruta2 = os.path.dirname(os.path.abspath(__file__))

documento = xlrd.open_workbook(ruta2+"/archivo.xlsx")

print(documento)

datos = documento.sheet_by_index(0) # Leyendo la primera hoja del documento

for i in range(datos.nrows):
    if i >= 1:
        print(f"ID={datos.cell_value(i,0)} | Nombre: {datos.cell_value(i,1)} | Apellido: {datos.cell_value(i,2)}")