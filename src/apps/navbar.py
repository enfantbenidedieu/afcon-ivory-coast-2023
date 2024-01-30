from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify


navbar = html.Div(className="header container-fluid p-2 mb-5 bg-black", children=[
    html.Div(className="bg-black d-flex flex-column flex-lg-row align-items-center justify-content-center justify-content-md-between", children=[
        html.Div(className="d-flex flex-column flex-lg-row align-items-center", children=[
            html.Div(className="d-flex flex-column flex-md-row align-items-center justify-content-center", children=[

                html.Div(className="fw-bold d-inline-block", children=[
                    html.H2(className="d-inline-block fw-bold align-items-center p-0", children=[
                        html.Span("Analytics", className="text-white"),
                        html.Span("Paper", className="text-danger")
                    ]),
                    html.Small("By Duvérier DJIFACK ZEBAZE", className="d-block text-muted fw-bold p-0", style={"font-size":"14px"})
                ])
            ]),
            
            html.Div(className="dash ms-lg-2 d-none d-xl-block"),

            html.Div(className="ms ms-lg-5 d-none d-xl-block", children=[
                html.H2("African Cup of Nations - Ivory Coast 2023",
                        className="title-header fw-bold"),
                html.H5("Keys Performance Indicator",
                        className="subtitle-header text-muted text-center text-md-start fw-bold")
            ]),
        ]),

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
    ])
])