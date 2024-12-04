import pandas as pd
import plotly.express as px
from dash import dcc, html, callback, Input, Output
from sqlalchemy import create_engine

#Datos de conexión
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

def dashboard1():
    fig = px.histogram(data, x="precio", nbins=20, title="Distribución de Precios", template="plotly_dark")
    fig.update_layout(xaxis_title="Precio", yaxis_title="Frecuencia")

    fig_box = px.scatter(
        data,
        x="precio_anterior",
        y="precio",
        size="descuento",
        color="descuento",
        hover_name="titulo",
        title="Relación entre Precios Actuales y Anteriores",
        template="plotly_dark"
    )
    fig_box.update_layout(xaxis_title="Precio Anterior", yaxis_title="Precio Actual")

    body = html.Div(
        [
            html.H3("Productos en Mercado Libre", style={"color": "white"}),
            html.P("Explora los datos de laptops extraídos de Mercado Libre", style={"color": "white"}),
            dcc.Dropdown(
                options=[
                    {"label": "Todos", "value": "all"},
                    {"label": "Precio", "value": "precio"},
                    {"label": "Precio Anterior", "value": "precio_anterior"},
                    {"label": "Descuento", "value": "descuento"}
                ],
                value="all",
                id="ddMetric"
            ),
            html.Hr(),
            dcc.Graph(figure=fig, id="figHist"),
            dcc.Graph(figure=fig_box, id="figScatter"),
        ],
        style={"background-color": "#000000", "padding": "10px"}
    )
    return body
