import pandas as pd
from sqlalchemy import create_engine

# Parámetros de conexión a MySQL
user = "root"
password = "Fr_8292004"
server = "localhost"
db = "mercadodb"

# Crear la cadena de conexión
cadena_conexion = f"mysql+mysqlconnector://{user}:{password}@{server}/{db}"

# Establecer conexión con la base de datos
engine = create_engine(cadena_conexion)  # Crear la conexión al MySQL
conexion = engine.connect()

# Cargar datos desde el archivo CSV limpio
csv_file = "C:/Users/aaron/PycharmProjects/ProyectoFinal/Datasets/productos_mercadolibre_limpio.csv"
df = pd.read_csv(csv_file)

# Insertar datos en la tabla productos_mercadolibre
df.to_sql("productos_mercadolibre", conexion, if_exists="replace", index=False)

# Confirmar la inserción de datos (opcional)
# Puedes ejecutar una consulta para verificar que los datos fueron insertados
sql = "SELECT * FROM productos_mercadolibre LIMIT 5"
df_check = pd.read_sql(sql, conexion)
print(df_check)

# Cerrar la conexión
conexion.close()
