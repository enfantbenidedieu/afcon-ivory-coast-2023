


from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_admin_components as dac


tab_compare = html.Div(
    children=[
        dbc.Row(html.H1("Model comparison")),
        html.Div([
            dac.SimpleBox(
                style={"height" : "500px","width":"100%"},
                title="Table summary metrics",
                width=12
            )
        ])
    ]
)