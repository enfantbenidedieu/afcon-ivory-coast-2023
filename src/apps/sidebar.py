

from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink('Overview',href = '/', active="exact",className="fa-solid fa-house"),
                dbc.NavLink("Database", href="/database", active="exact",className="fa-thin fa-database"),
                dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
                dbc.NavLink("Principal Components", href="/principal-component-analysis", active="exact"),
                dbc.NavLink("Logistic Regression", href="/logistic-regression", active="exact"),
                dbc.NavLink("Linear Discriminant", href="/linear-discriminant-analysis", active="exact"),
                dbc.NavLink("Classification Tree", href="/classification-and-regression-tree", active="exact"),
                dbc.NavLink("K nearest neighbors", href="/k-nearest-neighbors", active="exact"),
                dbc.NavLink("Comparaison des modèles", href="/model-compare", active="exact"),
                dbc.NavLink("Variable selection", href="/variable-selection", active="exact")
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=SIDEBAR_STYLE,
)