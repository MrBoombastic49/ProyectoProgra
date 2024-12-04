import pandas as pd
import plotly.express as px
from dash import dcc, html
from sqlalchemy import create_engine

# Parámetros de conexión a MySQL
user = "root"
password = "Fr_8292004"
server = "localhost"
db = "mercadodb"

# Crear la cadena de conexión
cadena_conexion = f"mysql+mysqlconnector://{user}:{password}@{server}/{db}"

# Establecer conexión con la base de datos
engine = create_engine(cadena_conexion)
conexion = engine.connect()

# Cargar datos desde la base de datos
sql = "SELECT * FROM productos_mercadolibre"
data = pd.read_sql(sql, conexion)

# Cerrar la conexión
conexion.close()

# Filtrar los productos que tienen reseñas
data = data[data['num_reviews'] > 0]

# Función para acortar nombres de productos
def shorten_title(title, max_length=15):
    if len(title) > max_length:
        return title[:max_length] + "..."
    return title

# Crear el dashboard
def dashboard3():
    # Aplicar la función de truncamiento
    data['titulo_corto'] = data['titulo'].apply(shorten_title)

    # Agrupar por nombre de producto y calcular la calificación promedio
    data_grouped = data.groupby('titulo_corto', as_index=False).agg({'calificacion': 'mean'})

    # Seleccionar los primeros 10 productos para la visualización
    data_grouped = data_grouped.head(10)

    # Crear el gráfico de barras simplificado
    fig_rating = px.bar(
        data_grouped,
        x="titulo_corto",
        y="calificacion",
        title="Promedio de Calificación de los 10 Principales Productos",
        template="plotly_dark",
        color="calificacion",
        labels={"titulo_corto": "Producto", "calificacion": "Calificación Promedio"},
        color_continuous_scale="Viridis"
    )

    fig_rating.update_layout(xaxis_title="Producto", yaxis_title="Calificación Promedio", xaxis_tickangle=-45)

    # Estructura del dashboard
    body = html.Div(
        [
            html.H3("Promedio de Calificación de los Productos", style={"color": "white"}),
            dcc.Graph(figure=fig_rating, id="figRating"),
        ],
        style={"background-color": "#000000", "padding": "10px"}
    )

    return body
