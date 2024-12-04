import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Input, Output

def welcome():
    body = html.Div(
        [
            html.H6("Proyecto Final: Mercado Libre"),

            html.Img(
                src="https://rappicard.mx/wp-content/uploads/2024/10/logo-mercado-libre.png",
                width=500,
                height=200,
                title="Python"
            ),

            html.P(
                "Objetivo: Identificar tendencias de precios, características técnicas y disponibilidad de laptops en Mercado Libre "
                "para facilitar la toma de decisiones de compra informada."
            ),

            html.Hr(),

            html.H4("Preguntas a Resolver:"),
            html.Ul(
                [
                    html.Li("¿Cuáles son los rangos de precios más comunes para las laptops según su marca y especificaciones técnicas?"),
                    html.Li("¿Cómo varían los precios de las laptops según su capacidad de almacenamiento y memoria RAM?"),
                    html.Li("¿Qué relación existe entre el precio promedio y las valoraciones de los productos por parte de los usuarios?"),
                ]
            ),

            html.Hr(),

            html.H4("Integrantes del Equipo:"),
            html.Ul(
                [
                    html.Li("Kristhof Arana Palafox <k1297909@uabc.edu.mx>"),
                    html.Li("Aaron Fernandez Pinto Lopez <fernandeza38@uabc.edu.mx>"),
                    html.Li("Frida Marisa Lopez Galaviz <frida.lopez40@uabc.edu.mx>"),
                    html.Li("Jesus Alexis Peralta Alarcon <jesus.peralta@uabc.edu.mx>"),
                ]
            ),
        ]
    )

    return body


