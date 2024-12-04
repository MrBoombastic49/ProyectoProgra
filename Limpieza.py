import pandas as pd

# Cargar el archivo CSV sucio
df = pd.read_csv("C:/Users/aaron/PycharmProjects/ProyectoFinal/Datasets/productos_mercadolibre_sucio.csv")

# Limpiar la columna de precios, eliminando el símbolo $ y las comas
df['precio'] = df['precio'].replace({r'[\$,]': ''}, regex=True).astype(float)

# Limpiar la columna de precios anteriores, eliminando el símbolo $ y las comas
df['precio_anterior'] = df['precio_anterior'].replace({r'[\$,]': ''}, regex=True).astype(float)

# Limpiar la columna de descuentos, eliminando el símbolo % y convirtiéndolo en número
df['descuento'] = df['descuento'].replace({r'%': ''}, regex=True).astype(float)

# Llenar valores NaN en la columna 'descuento' con 0 (por si algunos productos no tienen descuento)
df['descuento'] = df['descuento'].fillna(0)

# Asegurarse que las calificaciones sean numéricas, y mantener N/A como 'NaN' si no hay calificación
df['calificacion'] = pd.to_numeric(df['calificacion'], errors='coerce')  # Convierte 'N/A' a NaN

# Limpiar la columna de número de reseñas, reemplazando "N/A" por NaN y asegurándonos de que los valores sean enteros
df['num_reviews'] = df['num_reviews'].replace({'N/A': '0', r'[^\d]': ''}, regex=True)

# Reemplazar NaN en num_reviews por 0 y luego convertir a entero
df['num_reviews'] = df['num_reviews'].fillna(0).astype(int)

# Limpiar la columna de colores, reemplazando valores vacíos con "0" si es necesario
df['colores_disponibles'] = df['colores_disponibles'].fillna("0")

# Verificar que los datos estén limpios
print(df.head())

# Guardar el archivo limpio
df.to_csv("C:/Users/aaron/PycharmProjects/ProyectoFinal/Datasets/productos_mercadolibre_limpio.csv", index=False)
