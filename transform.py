# Importar las librerías necesarias
import pandas as pd

# Cargar el dataset a partir de la ruta establecida
df = pd.read_csv('co_properties.csv')

# Mantener las columnas relacionadas con ubicación
df = df[['id', 'lon', 'lat', 'l2', 'l3']]

# Exportar nuevo .csv
df.to_csv('co_properties_summary.csv', index=False, decimal='.')