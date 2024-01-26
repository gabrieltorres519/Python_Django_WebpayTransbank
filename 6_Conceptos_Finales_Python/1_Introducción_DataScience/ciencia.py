import pandas as pd 

archivo = pd.read_csv('train.csv')

print(archivo.head(20))
print(archivo.shape)

print(archivo['Id'])
print(archivo['SalePrice'].mean())
print(archivo.describe())

