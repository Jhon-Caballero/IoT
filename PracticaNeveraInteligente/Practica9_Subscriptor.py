import pandas as pd

# Lee el archivo Excel
archivo_excel = 'Mi unidad/Trabajos/IOT/RegistrosIoT.xlsx'  # Reemplaza con la ruta a tu archivo Excel
df = pd.read_excel(archivo_excel)

# Accede a los datos en la hoja de Excel
columna_nevera = df['nevera']
columna_producto = df['producto']
columna_cantidad = df['cantidad']
columna_pesos = df['pesos']

# Puedes imprimir los datos o realizar cualquier otra operación que necesites
print("Datos de la columna 'nevera':")
print(columna_nevera)

print("Datos de la columna 'producto':")
print(columna_producto)

print("Datos de la columna 'cantidad':")
print(columna_cantidad)

print("Datos de la columna 'pesos':")
print(columna_pesos)

