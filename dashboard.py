import welcome as w
import dash1 as d1
import dash2 as d2
import dash3 as d3
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, Dash, callback

@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return w.welcome()
    elif pathname == "/dash-1":
        return d1.dashboard1()
    elif pathname == "/dash-2":
        return d2.dashboard2()
    elif pathname == "/dash-3":
        return d3.dashboard3()
    # Página 404 para rutas no reconocidas

    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

def menu_dashboard():
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f3f37c",
    }

    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }

    sidebar = html.Div(
        [
            html.H2("Dashboard", className="display-6"),
            html.Hr(),
            html.P("Objetivo: comprender los datos de laptops en Mercado Libre", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Dashboard 1", href="/dash-1", active="exact"),
                    dbc.NavLink("Dashboard 2", href="/dash-2", active="exact"),
                    dbc.NavLink("Dashboard 3", href="/dash-3", active="exact"),
                    dbc.NavLink("Github", href="https://github.com/MrBoombastic49/ProyectoProgra", active="exact", target="_blank"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

    content = html.Div(id="page-content", style=CONTENT_STYLE)

    return html.Div([dcc.Location(id="url"), sidebar, content])

if __name__ == "__main__":
    app = Dash(external_stylesheets=[dbc.themes.MORPH], suppress_callback_exceptions=True)
    app.layout = menu_dashboard()
    app.run(debug=True)