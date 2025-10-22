#pip install pandas
import pandas as pd

df = pd.read_csv('bitcoin.csv') # Leer el csv y cargar los datos un DataFrame

print(df.head()) # 5 primeras filas
print(df.tail()) # 5 últimas filas
print(df.head().to_string()) # Muestra los datos sin truncar
df.info() # Información sobre columnas, número de no nulos por columnta y tipos
print(df.describe())