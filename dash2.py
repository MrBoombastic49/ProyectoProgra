import pandas as pd
import plotly.express as px
from dash import dcc, html, callback, Input, Output
from sqlalchemy import create_engine

# Parámetros de conexión a MySQL
user = "root"
password = "8292004"
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

def dashboard2():
    # Relación entre el precio y el descuento
    fig_price_discount = px.scatter(
        data,
        x="precio",
        y="descuento",
        title="Relación entre Precio y Descuento",
        template="plotly_dark",
        labels={"precio": "Precio", "descuento": "Descuento (%)", "titulo": "Producto"},  # Agregar nombre del producto en labels
        color="descuento",
        hover_name="titulo"  # Muestra el nombre del producto cuando se pasa el cursor
    )
    fig_price_discount.update_layout(xaxis_title="Precio", yaxis_title="Descuento (%)")

    body = html.Div(
        [
            html.H3("Explora la relación entre Precio y Descuento", style={"color": "white"}),
            dcc.Graph(figure=fig_price_discount, id="figPriceDiscount"),
        ],
        style={"background-color": "#000000", "padding": "10px"}
    )
    return body