# -*- coding: utf-8 -*-

from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import dash_mantine_components as dmc


navbar = dbc.Navbar(
        dbc.Container(
            children=[
                html.A(
                    dbc.Row(
                        children=[
                            dbc.Col(html.Img(id="logo",src="/static/images/afcon_2023.png",style={'height':'50px','width':'150px'})),
                            dbc.Col(dbc.NavbarBrand([html.H1("Africa Cup of Nations - Ivory Coast 2023",style={"color":"white"})], className="ms-2")),
                        ],
                        align="center",
                    ),
                    href="https://www.cafonline.com/caf-africa-cup-of-nations/",
                    style={"textDecoration": "none"},
                ),
                html.Div(className="mt-4 mt-lg-0", children=[
                    dbc.Nav(className="ms-auto d-flex flex-row align-items-center justify-content-center", navbar=True, children=[
                        dmc.Tooltip(
                            label="Code source",
                            position="bottom",
                            withArrow=True,
                            arrowSize=6,
                            color="black",
                            transition="scale",
                            transitionDuration=300,
                            ff="serif",
                            className="m3 ms-3",
                            children=[
                            dbc.Button(href="https://github.com/enfantbenidedieu/afcon-ivory-coast-2023", className="btn", children=[
                                DashIconify(icon="radix-icons:github-logo",
                                            width=30), " Voir sur github"
                            ])
                            ]
                        )
                    ])
                ])
            ],
            fluid=True,
        ),
        dark=True,
        color="black",
        sticky="top",
        id="id_navbar"
    )



