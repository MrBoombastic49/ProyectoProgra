import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Input, Output


def welcome():
    body = html.Div(
        [
            html.Div(
                [
                    html.H1("Proyecto Final: Mercado Libre", style={"textAlign": "center", "color": "#0056A2"}),

                    html.Img(
                        src="https://images-ext-1.discordapp.net/external/E-TjAT8zZrtS6XPJzh27wFK_8szolUiwvkbAoL6w0KU/https/cdn.dribbble.com/users/1490688/screenshots/5467268/media/907ab1b783121ab1f1aaa976e5edee56.gif?width=625&height=469",
                        style={"display": "block", "margin": "20px auto", "width": "300px", "height": "auto"},
                        title="Python"
                    ),

                    html.P(
                        (
                            "Objetivo: Identificar tendencias de precios, características técnicas y disponibilidad de laptops en "
                            "Mercado Libre para facilitar la toma de decisiones de compra informada."
                        ),
                        style={"textAlign": "justify", "fontSize": "16px", "lineHeight": "1.6"},
                    ),
                ],
                style={"padding": "20px", "backgroundColor": "#F9F9F9", "borderRadius": "10px",
                       "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)"},
            ),

            html.Hr(style={"margin": "30px 0"}),

            html.Div(
                [
                    html.H4("Preguntas a Resolver:", style={"color": "#333", "marginBottom": "15px"}),

                    html.Ul(
                        [
                            html.Li(
                                "¿Cuáles son los rangos de precios más comunes para las laptops según su marca y especificaciones técnicas?"),
                            html.Li(
                                "¿Cómo varían los precios de las laptops según su capacidad de almacenamiento y memoria RAM?"),
                            html.Li(
                                "¿Qué relación existe entre el precio promedio y las valoraciones de los productos por parte de los usuarios?"),
                        ],
                        style={"lineHeight": "1.8", "paddingLeft": "20px", "fontSize": "15px"},
                    ),
                ],
                style={"marginBottom": "30px"},
            ),

            html.Hr(style={"margin": "30px 0"}),

            html.Div(
                [
                    html.H4("Integrantes del Equipo:", style={"color": "#333", "marginBottom": "15px"}),

                    html.Ul(
                        [
                            html.Li("Kristhof Arana Palafox <k1297909@uabc.edu.mx>"),
                            html.Li("Aaron Fernandez Pinto Lopez <fernandeza38@uabc.edu.mx>"),
                            html.Li("Frida Marisa Lopez Galaviz <frida.lopez40@uabc.edu.mx>"),
                            html.Li("Jesus Alexis Peralta Alarcon <jesus.peralta@uabc.edu.mx>"),
                        ],
                        style={"lineHeight": "1.8", "paddingLeft": "20px", "fontSize": "15px"},
                    ),
                ],
                style={"marginBottom": "30px"},
            ),
        ],
        style={"fontFamily": "Arial, sans-serif", "color": "#333", "maxWidth": "800px", "margin": "0 auto",
               "padding": "20px"},
    )

    return body

