import pandas as pd
from pandas import ExcelWriter
import os


ruta2 = os.path.dirname(os.path.abspath(__file__))

datos = pd.DataFrame({ # DataFrame con la información a cargar en el archivo excel
    'id':[1,2,3,4],
    'nombre': ["Juan", "Gabriel", "Maria", "Felipe"],
    'apellido': ["Martinez", "Pérez", "Torres", "Montana"]
})

datos = datos[['id','nombre','apellido']]

writer = pd.ExcelWriter(ruta2+"/archivo.xlsx")

datos.to_excel(writer, "Hoja 1", index=False)

writer._save()